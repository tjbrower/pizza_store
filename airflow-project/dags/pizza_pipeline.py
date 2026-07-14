from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

with DAG(
    dag_id='pizza_pipeline',
    schedule='@daily',
    start_date=datetime(2024, 1, 1),
    catchup=False
) as dag:

    task_ingest = BashOperator(
        task_id='ingest_data',
        bash_command='python /usr/local/airflow/include/ingest.py'
    )

    task_dbt_run = BashOperator(
        task_id='dbt_run',
        bash_command='dbt run --project-dir /usr/local/airflow/include --profiles-dir /usr/local/airflow/include'
    )

    task_dbt_test = BashOperator(
        task_id='dbt_test',
        bash_command='dbt test --project-dir /usr/local/airflow/include --profiles-dir /usr/local/airflow/include'
    )

    task_ingest >> task_dbt_run >> task_dbt_test