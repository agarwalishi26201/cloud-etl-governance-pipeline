from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.empty import EmptyOperator
from airflow.operators.python import PythonOperator

default_args = {
    'owner': 'data-eng-team',
    'depends_on_past': False,
    'email_on_failure': True,
    'email': ['alerts@example.com'],
    'retries': 2,
    'retry_delay': timedelta(minutes=5),
}

def run_security_ingestion(**context):
    execution_date = context['ds']
    print(f"Starting idempotent ingestion for partition date: {execution_date}")
    # Simulates loading logs into partitioned storage safely

with DAG(
    'enterprise_security_governance_etl',
    default_args=default_args,
    description='Idempotent daily ETL pipeline for telemetry and security logs',
    schedule_interval='@daily',
    start_date=datetime(2026, 1, 1),
    catchup=False,
    tags=['security', 'etl', 'governance'],
) as dag:

    start_task = EmptyOperator(task_id='pre_flight_check')

    ingest_task = PythonOperator(
        task_id='ingest_and_partition_logs',
        python_callable=run_security_ingestion,
        provide_context=True,
    )

    validate_task = EmptyOperator(task_id='schema_and_quality_validation')

    end_task = EmptyOperator(task_id='pipeline_complete')

    start_task >> ingest_task >> validate_task >> end_task
