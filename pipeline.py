from airflow.operators.python import PythonOperator
from airflow import DAG
import kaggle as kg
import os
import boto3
from datetime import datetime, timedelta
from dotenv import load_dotenv

load_dotenv()

access_key = os.getenv('access_key')
secret_key = os.getenv('secret_key')
bucket_name = os.getenv('bucket_name')

default_args = {
    'owner': 'Sampath005',
    'depends_on_past': False,
    'email_on_failure': True,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
    'start_date': datetime(2024, 3, 16),
}


def download_dataset():
    try:
        kg.api.authenticate()
        kg.api.dataset_download_files(dataset="dataset-name", path='on.zip', unzip=True)
        return True
    except Exception as e:
        print(f"An error occurred during dataset download: {e}")
        return False


def upload_files_to_s3(file_path):
    s3_client = boto3.client('s3', aws_access_key_id=access_key, aws_secret_access_key=secret_key)

    try:
        response = s3_client.upload_file(file_path, bucket_name, 'Output.csv')
        return 'file uploaded'
    except Exception as e:
        return f"Failed to upload file {file_path} to bucket {bucket_name} with error: {e}"


with DAG('my_dag', default_args=default_args, schedule_interval='@daily') as dag:
    task1 = PythonOperator(
        task_id='download_dataset',
        python_callable=download_dataset,
        dag=dag
    )
    task2 = PythonOperator(
        task_id='write_dataset',
        python_callable=upload_files_to_s3,
        op_kwargs={
            "file_path": 'file/path/input.csv'
        },
        dag=dag
    )

    task1 >> task2


