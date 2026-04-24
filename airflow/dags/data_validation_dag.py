from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import sys
import os

# Add src to path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../src')))

from main import main_pipeline

default_args = {
    'owner': 'akhil',
    'start_date': datetime(2024, 1, 1),
    'retries': 1
}

with DAG(
    'data_validation_pipeline',
    default_args=default_args,
    schedule_interval='@daily',
    catchup=False
) as dag:

    run_pipeline = PythonOperator(
        task_id='run_validation',
        python_callable=main_pipeline
    )