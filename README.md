# 🚀 End-to-End ETL Pipeline using Apache Airflow, Docker & AWS S3

![Airflow](https://img.shields.io/badge/Airflow-2.9-blue)
![AWS](https://img.shields.io/badge/AWS-S3-orange)
![Docker](https://img.shields.io/badge/Docker-Containerized-blue)

---
## 📌 Overview

This project demonstrates an end-to-end **ETL (Extract, Transform, Load)** pipeline using **Apache Airflow**, **Docker**, and **AWS S3**.

The pipeline:

* Extracts data from a public API
* Transforms it using Pandas
* Loads the processed data into AWS S3
---

## 🏗️ Architecture

```
        +----------------------+
        |   Public API         |
        +----------+-----------+
                   |
                   v
        +----------------------+
        |   Apache Airflow     |
        |  (Scheduler + DAGs)  |
        +----------+-----------+
                   |
        +----------+-----------+
        |                      |
        v                      v
+----------------+     +----------------+
|   Transform    |     |   Logging      |
| (Pandas)       |     | (Airflow Logs) |
+----------------+     +----------------+
                   |
                   v
        +----------------------+
        |      AWS S3          |
        | (Final Output Data)  |
        +----------------------+
```
---

## ⚙️ Tech Stack

* Apache Airflow
* Python (Pandas, Requests, Boto3)
* Docker
* AWS S3
---
## 🔄 Workflow
1. **Extract**
   * Fetch data from a public API using `requests`
2. **Transform**
   * Clean and process data using `pandas`
   * Example: Add derived columns like `title_length`
3. **Load**
   * Upload processed data to AWS S3 bucket using `boto3`
---
## ▶️ How to Run
### 1. Clone the repository
```
git clone https://github.com/paneeshreddy/open-meteo-elt-pipeline.git
cd open-meteo-elt-pipeline
```
### 2. Start Airflow
```
docker compose up -d
```
### 3. Access Airflow UI
```
http://localhost:8080
```
---
## 🔐 Environment Setup
Create a `.env` file (DO NOT commit this file):
```
AWS_ACCESS_KEY_ID=your_access_key
AWS_SECRET_ACCESS_KEY=your_secret_key
AWS_DEFAULT_REGION=us-east-2
```
---
## 🔐 Security
* AWS credentials are managed using environment variables
* No secrets are stored in code
* `.env` file is excluded via `.gitignore`
---

## 📂 Project Structure
```
.
├── dags/
│   └── db2_to_lambda_pipeline.py
├── docker-compose.yaml
├── README.md
```
---
## 📊 Sample Output
Example of transformed dataset:

| userId | title_length |
| ------ | ------------ |
| 1      | 45           |
| 2      | 32           |
| 3      | 28           |
---
## 📈 Airflow DAG

* DAG Name: `db2_to_lambda_pipeline`
* Tasks:

  * extract
  * transform
  * load
---
## 🚀 Future Improvements
* Add AWS Lambda trigger after S3 upload
* Implement data validation (Great Expectations)
* Add monitoring & alerting (Slack / Email)
* Integrate with data warehouse (Snowflake / Redshift)
---
## 💼 Key Learnings
* Built a production-style ETL pipeline
* Orchestrated workflows using Apache Airflow
* Integrated cloud storage (AWS S3)
* Implemented secure credential handling
* Containerized application using Docker
---
## 👤 Author

**Aneesh Pasnoor
