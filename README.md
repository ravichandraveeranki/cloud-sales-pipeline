# Cloud Sales Pipeline

## Overview
This project simulates a cloud-style sales analytics pipeline using Python, PySpark-ready structure, Airflow orchestration, and SQL reporting.

## Components
- `scripts/` → extract, transform, load pipeline modules
- `dags/` → Airflow DAG for scheduled ETL execution
- `data/` → source and output datasets
- `sql/` → reporting queries
- `requirements.txt` → project dependencies

## Tech Stack
- Python
- Pandas
- PySpark
- Apache Airflow
- SQL
- PostgreSQL
- AWS S3 (planned extension)

## Workflow
1. Extract sales, customer, and product data
2. Transform data into analytics-ready format
3. Load final output dataset
4. Orchestrate ETL using Airflow DAG
5. Query outputs with SQL

## Run Locally

```bash
python main.py
## PySpark Version
This project also includes a PySpark-based ETL workflow for scalable processing.

Run it with:

```bash
python main_spark.py