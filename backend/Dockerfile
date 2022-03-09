FROM python:3.8-slim

WORKDIR /sitreps/

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY ./sitreps_server /sitreps/sitreps_server/
EXPOSE 8000
EXPOSE 5432

CMD ["uvicorn", "sitreps_server.main:app", "--host","0.0.0.0", "--port","8000"]
