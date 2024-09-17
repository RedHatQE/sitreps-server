[![sitreps-server](https://github.com/RedHatQE/sitreps-server/actions/workflows/tests.yaml/badge.svg?branch=main)](https://github.com/RedHatQE/sitreps-server/actions/workflows/tests.yaml)

# sitreps-server
Sitreps, short for `Situation Reports`, is a tool designed to analyze the status of applications. It helps observe and analyze various project-related metrics using Grafana dashboard visualizations. This code repository contains the source code for the backend of Sitreps, which provides the REST API.

## Development environment

### Running locally
To create an `.env` file in your home directory for holding configuration required for running sitreps:

```bash
POSTGRESQL_SERVER=localhost
POSTGRESQL_PORT=5432
POSTGRESQL_DATABASE=sitreps
POSTGRESQL_USER=admin
POSTGRESQL_PASSWORD=admin
GF_AUTH_BASIC_ENABLED=true
GF_SECURITY_ADMIN_USER=admin
GF_SECURITY_ADMIN_PASSWORD=admin
GF_AUTH_ANONYMOUS_ENABLED=true
GF_AUTH_ANONYMOUS_ORG_ROLE=Viewer
```

Uses `podman-compose` to deploy the individual components and supporting containers.

```bash
podman-compose up --build # Build images if needed and start containers
podman-compose down       # Stop and remove containers
```

### Accessing the URLs
- Grafana Instance: http://localhost:3000
- Sitreps API: http://localhost:8000

Make sure that your local services are running on these ports and are accessible for successful integration and testing.

### OpenAPI docs
Our REST API is documented using OpenAPI v3. On a local instance it can be accessed [here](http://localhost:8000/docs)

## [Grafana](http://localhost:3000):
This used to visualize the metrics collected by sitreps. Grafana connects to the data source where sitreps stores its metrics and allows you to create dashboards, charts, and other visualizations to analyze the data.

### Add a Data Source:
Go to Grafana's data source settings.
Add a new data source and configure it to point to the data store or API where sitreps is storing the metrics.

We are configuring the following datasources:

- PostgreSQL
  ```
  Name: db
  Host URL: db:5432
  Database Name: sitreps
  Username: admin
  Password: admin
  Infinity
  ```

- Sitreps-APIs
  ```
  Name: apis
  Authentication: No Auth
  Infinity
  ```

- GitLab APIs
  ```
  Name: gitlab-api
  Authentication: Bearer Token
  Allowed Hosts: <GitLab URL>
  Network:
    With CA Cert: Current-IT-Root-CAs.pem
  ```

### Create Dashboards:
Create new dashboards and panels to visualize the metrics. Use Grafana’s query editor to fetch and display the metrics from the data source.

We are maintaining datasources for the Grafana dashboard, which include a shareable backup of the production datasources. These datasources can be imported as needed.


### Dashboards Backup:
We have a customized script for backing up Grafana dashboards, which utilizes Grafana APIs. The default APIs provide a complete backup of dashboards, but this backup includes sensitive data that cannot be shared. While the Grafana UI allows for exporting sharable dashboards, manual export is not feasible every time.

To address this, we have reverse-engineered a method to export sharable dashboards. This script facilitates the backup process by producing a sharable version of the dashboards.

Usage:
```
python grafana.py --backup --host <grafana_url>
```

```
python grafana.py -h

usage: grafana.py [-h] [--backup] [--restore] [--host HOST] [--api-key API_KEY]

Backup and Restore Grafana Dashboards.

options:
  -h, --help         show this help message and exit
  --backup           Backup dashboards.
  --restore          Restore dashboards.
  --host HOST        Grafana hostname. Default http://localhost:3000
  --api-key API_KEY  Grafana API key
```

### Running tests
[WIP]
