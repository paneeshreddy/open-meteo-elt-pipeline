from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import requests
import pandas as pd
import boto3


RAW_PATH = "/opt/airflow/dags/raw_weather.csv"
PROCESSED_PATH = "/opt/airflow/dags/processed_weather.csv"
OUTPUT_PATH = "/opt/airflow/dags/final_weather.csv"

S3_BUCKET = "airflow-etl-aneesh-2026"
S3_KEY = "weather/final_weather.csv"


# EXTRACT: Get weather data from Open-Meteo API
def extract():
    url = (
        "https://api.open-meteo.com/v1/forecast"
        "?latitude=40.7128"
        "&longitude=-74.0060"
        "&hourly=temperature_2m,relative_humidity_2m,wind_speed_10m"
        "&forecast_days=1"
        "&timezone=auto"
    )

    response = requests.get(url, timeout=30)
    response.raise_for_status()

    data = response.json()

    hourly = data["hourly"]

    df = pd.DataFrame({
        "timestamp": hourly["time"],
        "temperature_c": hourly["temperature_2m"],
        "humidity_percent": hourly["relative_humidity_2m"],
        "wind_speed_kmh": hourly["wind_speed_10m"]
    })

    df.to_csv(RAW_PATH, index=False)

    print(f"Extracted {len(df)} weather records.")


# TRANSFORM: Clean and process weather data
def transform():
    df = pd.read_csv(RAW_PATH)

    df["timestamp"] = pd.to_datetime(df["timestamp"])

    df["temperature_f"] = (
        df["temperature_c"] * 9 / 5
    ) + 32

    df["temperature_c"] = df["temperature_c"].round(2)
    df["temperature_f"] = df["temperature_f"].round(2)
    df["humidity_percent"] = df["humidity_percent"].round(2)
    df["wind_speed_kmh"] = df["wind_speed_kmh"].round(2)

    df.to_csv(PROCESSED_PATH, index=False)

    print(f"Transformed {len(df)} weather records.")


# LOAD: Upload processed data to Amazon S3
def load():
    df = pd.read_csv(PROCESSED_PATH)

    df.to_csv(OUTPUT_PATH, index=False)

    s3 = boto3.client("s3")

    s3.upload_file(
        OUTPUT_PATH,
        S3_BUCKET,
        S3_KEY
    )

    print(
        f"Uploaded processed weather data to "
        f"s3://{S3_BUCKET}/{S3_KEY}"
    )


# DAG definition
dag = DAG(
    dag_id="weather_etl_pipeline",
    start_date=datetime(2024, 1, 1),
    schedule="@daily",
    catchup=False,
)


# Tasks
t1 = PythonOperator(
    task_id="extract_weather_data",
    python_callable=extract,
    dag=dag,
)

t2 = PythonOperator(
    task_id="transform_weather_data",
    python_callable=transform,
    dag=dag,
)

t3 = PythonOperator(
    task_id="load_weather_data_to_s3",
    python_callable=load,
    dag=dag,
)


# Pipeline flow
t1 >> t2 >> t3
