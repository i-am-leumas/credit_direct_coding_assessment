# incremental_dag.py

from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.mysql_to_gcs import MySqlToGoogleCloudStorageOperator
from airflow.operators.gcs_to_bq import GoogleCloudStorageToBigQueryOperator

default_args = {
    'owner': 'senior_data_engineer',
    'depends_on_past': False,
    'start_date': datetime(2023, 8, 1),
    'email_on_failure': False,
    'email_on_retry': False,
}

with DAG(
    'incremental_dag',
    schedule_interval=timedelta(days=1),  # Daily schedule
    default_args=default_args,
    catchup=False,
) as dag:

    # MySQL to GCS Operator
    mysql_to_gcs = MySqlToGoogleCloudStorageOperator(
        task_id='mysql_to_gcs',
        sql='SELECT * FROM employees WHERE last_update >= {{ execution_date }} - INTERVAL 1 DAY',
        bucket='your-gcs-bucket',
        filename='employees_data_daily.csv',
        mysql_conn_id='mysql_conn',
        gcp_conn_id='gcp_conn',
    )

    # GCS to BigQuery Operator
    gcs_to_bq = GoogleCloudStorageToBigQueryOperator(
        task_id='gcs_to_bigquery',
        bucket='your-gcs-bucket',
        source_objects=['employees_data_daily.csv'],
        destination_project_dataset_table='your_project_id.dataset_id.employees',
        autodetect=True,
        write_disposition='WRITE_APPEND',
        bigquery_conn_id='bigquery_conn',
    )

    # Define task dependencies
    mysql_to_gcs >> gcs_to_bq
