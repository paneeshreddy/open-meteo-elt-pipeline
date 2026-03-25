from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import requests
import pandas as pd
import boto3


# 🔹 EXTRACT: Get data from API
def extract():
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)
    data = response.json()

    df = pd.DataFrame(data)
    df.to_csv("/opt/airflow/dags/raw_data.csv", index=False)

    print("Extracted data and saved to raw_data.csv")


# 🔹 TRANSFORM: Clean & process
def transform():
    df = pd.read_csv("/opt/airflow/dags/raw_data.csv")

    # Example transformation
    df["title_length"] = df["title"].apply(len)

    df.to_csv("/opt/airflow/dags/processed_data.csv", index=False)

    print("Transformed data and saved to processed_data.csv")


# 🔹 LOAD: Save locally + upload to S3
def load():
    # Read processed file
    df = pd.read_csv("/opt/airflow/dags/processed_data.csv")

    # Save final output locally
    output_path = "/opt/airflow/dags/final_output.csv"
    df.to_csv(output_path, index=False)

    # Upload to S3
    s3 = boto3.client("s3")

    s3.upload_file(
        output_path,
        "airflow-etl-aneesh-2026",   # 🔁 your bucket name
        "final_output.csv"
    )

    print("Uploaded to S3 successfully")


# 🔹 DAG definition
dag = DAG(
    dag_id="db2_to_lambda_pipeline",
    start_date=datetime(2024, 1, 1),
    schedule="@daily",
    catchup=False,
)


# 🔹 Tasks
t1 = PythonOperator(
    task_id="extract",
    python_callable=extract,
    dag=dag,
)

t2 = PythonOperator(
    task_id="transform",
    python_callable=transform,
    dag=dag,
)

t3 = PythonOperator(
    task_id="load",
    python_callable=load,
    dag=dag,
)

# 🔗 Pipeline flow
t1 >> t2 >> t3
