from datetime import datetime
from airflow import DAG
from airflow.operators.python import PythonOperator
from scripts.extract import extract
from scripts.transform import transform
from scripts.load import load


def run_pipeline():
    customers, products, sales = extract()
    sales_data = transform(customers, products, sales)
    load(sales_data)


with DAG(
    dag_id="sales_pipeline",
    start_date=datetime(2025, 1, 1),
    schedule_interval="@daily",
    catchup=False,
) as dag:

    run_etl = PythonOperator(
        task_id="run_etl_pipeline",
        python_callable=run_pipeline
    )