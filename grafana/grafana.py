"""Grafana CLI Options.

This script allows for backing up and restoring Grafana dashboards. It supports:
- Backup of dashboards for external upload.
- Need to add proper support for restoration of dashboards from backup files.
"""

import argparse
import json
import os
import pathlib
import re
from functools import cached_property
from urllib.parse import urljoin

import requests

# Define the directory where backup files will be stored
PARENT_DIR = pathlib.Path(__file__).parent.resolve()
SITREPS_API_REGEX = r"^http://[^/]+:8000+"


class Grafana:
    """A class to interact with Grafana's API for managing dashboards."""

    def __init__(self, host: str, api_key: str = None):
        """Initializes the Grafana instance.

        Args:
            host (str): The base URL of the Grafana instance.
            api_key (str, optional): The API key for authenticating requests.
        """
        self.host = host
        self.api_key = api_key

    @property
    def headers(self):
        """Returns the headers for API requests."""
        return {"Authorization": f"Bearer {self.api_key}", "Content-Type": "application/json"}

    @cached_property
    def datasources(self) -> dict | None:
        """Fetches and caches the available datasources from Grafana."""
        datasources = {}
        url = urljoin(self.host, "/api/datasources")
        response = requests.get(url, headers=self.headers)

        if response.status_code == 200:
            for ds in response.json():
                datasources[ds["uid"]] = {
                    "name": ds["name"].replace("-", "_").upper(),
                    "label": ds["name"],
                    "description": "",
                    "type": "datasource",
                    "pluginId": ds["type"],
                    "pluginName": ds["typeName"],
                }
            return datasources
        else:
            print(f"Failed to fetch datasources: {response.status_code} - {response.text}")
            return None

    def _external_sharable(self, dashboard: dict) -> dict:
        """Prepares a dashboard for external sharing by updating datasource references.

        Args:
            dashboard (dict): The dashboard JSON data.

        Returns:
            dict: The updated dashboard JSON data.
        """
        datasources = self.datasources
        applicable_ds = []

        def _search_replace_datasource(obj):
            if isinstance(obj, dict):
                for key, value in obj.items():
                    if key == "annotations":
                        continue
                    # Replace datasource UID with variable.
                    if key == "datasource" and isinstance(value, dict):
                        if uid := value.get("uid"):
                            if uid in datasources:
                                applicable_ds.append(uid)
                                ds_name = datasources[uid]["name"]
                                value["uid"] = f"${{{ds_name}}}"
                    # Replace sitreps API's UIL with Variable.
                    elif key == "url" and re.search(SITREPS_API_REGEX, value):
                        obj[key] = re.sub(SITREPS_API_REGEX, "${SITREPS_API}", value)
                    else:
                        _search_replace_datasource(value)
            elif isinstance(obj, list):
                for item in obj:
                    _search_replace_datasource(item)

        _search_replace_datasource(dashboard)
        inputs = [datasources.get(ds_uid) for ds_uid in set(applicable_ds)]

        # If sitreps apis used by dashobard then include input asking hostname for sitreps apis.
        if "APIS" in [ds["name"] for ds in inputs]:
            inputs.append(
                {
                    "name": "SITREPS_API",
                    "label": "sitreps_api",
                    "description": "Sitreps API endpoint.",
                    "type": "constant",
                }
            )

        dashboard["__inputs"] = inputs
        return dashboard

    def backup(self):
        """Fetches and backs up all dashboards from Grafana."""
        search_url = urljoin(self.host, "/api/search?query=&type=dash-db")
        response = requests.get(search_url, headers=self.headers)

        if response.status_code == 200:
            dashboards = response.json()
            if not dashboards:
                print("No dashboards found.")
                return

            for dashboard in dashboards:
                dashboard_uid = dashboard["uid"]
                dashboard_url = urljoin(self.host, f"/api/dashboards/uid/{dashboard_uid}")
                dashboard_response = requests.get(dashboard_url, headers=self.headers)

                if dashboard_response.status_code == 200:
                    dashboard_data = dashboard_response.json().get("dashboard", {})
                    dashboard_data = self._external_sharable(dashboard_data)
                    backup_filename = PARENT_DIR / f"{'-'.join(dashboard['title'].split())}.json"
                    with open(backup_filename, "w") as file:
                        json.dump(dashboard_data, file, indent=4)
                    print(f"Dashboard {dashboard['title']} backed up successfully.")
                else:
                    print(
                        f"Failed to back up dashboard {dashboard['title']}: {dashboard_response.status_code} - {dashboard_response.text}"
                    )
        else:
            print(f"Failed to fetch dashboards: {response.status_code} - {response.text}")

    def restore(self):
        """Restores dashboards from backup files."""
        for file_path in PARENT_DIR.glob("*.json"):
            with open(file_path) as file:
                dashboard_data = json.load(file)
                if "dashboard" in dashboard_data:
                    dashboard_data["overwrite"] = True

                restore_url = urljoin(self.host, "/api/dashboards/db")
                response = requests.post(
                    restore_url, headers=self.headers, data=json.dumps(dashboard_data)
                )

                if response.status_code == 200:
                    print(f"Dashboard from {file_path} restored successfully.")
                else:
                    print(
                        f"Failed to restore dashboard from {file_path}: {response.status_code} - {response.text}"
                    )


def main():
    """Handle command-line arguments and invoke backup or restore operations."""
    parser = argparse.ArgumentParser(description="Backup and Restore Grafana Dashboards.")
    parser.add_argument("--backup", action="store_true", help="Backup dashboards.")
    parser.add_argument("--restore", action="store_true", help="Restore dashboards.")
    parser.add_argument("--host", type=str, help="Grafana hostname. Default http://localhost:3000")
    parser.add_argument("--api-key", type=str, help="Grafana API key")

    args = parser.parse_args()
    host = args.host or os.environ.get("SITREPS_HOSTNAME") or "http://localhost:3000"
    grafana = Grafana(host=host, api_key=args.api_key)

    if args.backup:
        print("Taking backup of all dashboards...")
        grafana.backup()
    elif args.restore:
        print("Restoring all dashboards...")
        grafana.restore()
    else:
        print("Please specify --backup or --restore option.")


if __name__ == "__main__":
    main()
