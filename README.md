# 🚀 Open-Meteo ETL Pipeline

A containerized end-to-end data engineering pipeline that extracts weather data from a public API, transforms it using Python and Pandas, and loads the processed data into Amazon S3 using Apache Airflow for workflow orchestration.

---

## 📌 Overview

This project demonstrates a production-style ETL workflow using:

- Apache Airflow
- Python
- Pandas
- Requests
- Boto3
- Docker
- Amazon S3

The pipeline follows:

**Extract → Transform → Load**

1. Extract weather data from a public API.
2. Transform and clean the data using Pandas.
3. Load the processed dataset into Amazon S3.
4. Use Apache Airflow to orchestrate and monitor the workflow.

---

## 🏗️ Architecture

```text
                 Public Weather API
                         |
                         | Extract
                         v
                +-------------------+
                |   Apache Airflow  |
                |       DAG         |
                +---------+---------+
                          |
                          v
                +-------------------+
                | Python + Pandas   |
                | Transformation    |
                +---------+---------+
                          |
                          | Load
                          v
                +-------------------+
                |     Amazon S3     |
                | Processed Dataset |
                +-------------------+

              Docker / Docker Compose
              runs the Airflow environment
```

---

## 🔄 Data Flow

### 1. Extract

The Airflow DAG retrieves data from a public weather API using Python and `requests`.

### 2. Transform

The extracted data is processed using Pandas.

Transformations include:

- Cleaning raw API data
- Selecting required fields
- Creating derived columns
- Preparing analytics-ready records

### 3. Load

The transformed dataset is uploaded to Amazon S3 using `boto3`.

### 4. Orchestration

Apache Airflow manages the workflow, task dependencies, scheduling, and execution logs.

---

## 🛠️ Technology Stack

| Technology | Purpose |
|---|---|
| Python | Pipeline development |
| Apache Airflow | Workflow orchestration |
| Pandas | Data transformation |
| Requests | API data extraction |
| Boto3 | AWS integration |
| Amazon S3 | Cloud data storage |
| Docker | Containerization |
| Docker Compose | Local environment |

---

## 📂 Project Structure

```text
open-meteo-elt-pipeline/
├── dags/
│   └── <airflow_dag>.py
├── docker-compose.yaml
├── .gitignore
├── requirements.txt
└── README.md
```

---

## ▶️ How to Run

### 1. Clone the repository

```bash
git clone https://github.com/paneeshreddy/open-meteo-elt-pipeline.git
cd open-meteo-elt-pipeline
```

### 2. Start the Airflow environment

```bash
docker compose up -d
```

### 3. Open the Airflow UI

Open:

```text
http://localhost:8080
```

From the Airflow UI, enable and trigger the ETL DAG.

---

## 🔐 Environment Setup

Create a `.env` file locally and **do not commit it**.

```text
AWS_ACCESS_KEY_ID=your_access_key
AWS_SECRET_ACCESS_KEY=your_secret_key
AWS_DEFAULT_REGION=us-east-2
```

AWS credentials should be provided through environment variables or another secure credential mechanism.

---

## 🔒 Security

- AWS credentials are not stored in source code.
- Sensitive configuration is provided through environment variables.
- `.env` is excluded through `.gitignore`.
- No AWS secrets should be committed to the repository.

---

## 📊 Example Output

Example of a processed dataset:

| userId | title_length |
|---:|---:|
| 1 | 45 |
| 2 | 32 |
| 3 | 28 |

---

## 📈 Airflow DAG

The Airflow DAG contains three primary stages:

```text
Extract
   ↓
Transform
   ↓
Load
```

Airflow provides scheduling, task orchestration, dependency management, and execution logging.

> **Note:** Replace `<airflow_dag>.py` above with the actual DAG filename in the repository.

---

## 🚀 Future Improvements

- Add AWS Lambda integration after S3 upload
- Implement data-quality validation
- Add monitoring and alerting
- Add retry and failure-notification strategies
- Integrate with Snowflake or Amazon Redshift
- Add automated CI testing with GitHub Actions

---

## 💼 Key Learnings

- Built an end-to-end ETL pipeline using Python and Apache Airflow
- Orchestrated data workflows using Airflow DAGs
- Integrated Python pipelines with Amazon S3
- Performed data transformation using Pandas
- Containerized the development environment using Docker
- Implemented secure handling of AWS credentials

---

## 👤 Author

**Aneesh Pasnoor**
