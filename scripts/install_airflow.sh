#!/bin/bash

export AIRFLOW_VERSION=2.5.0
export PYTHON_VERSION="$(python --version | cut -d " " -f 2 | cut -d "." -f 1-2)"
export AIRFLOW_EXTRA_PROVIDERS=("amazon" "google" "apache" "sftp")
export AIRFLOW_CONSTRAINT_URL="https://raw.githubusercontent.com/apache/airflow/constraints-${AIRFLOW_VERSION}/constraints-${PYTHON_VERSION}.txt"
pip install "apache-airflow[async,postgres,google]==${AIRFLOW_VERSION}" --constraint "${AIRFLOW_CONSTRAINT_URL}"