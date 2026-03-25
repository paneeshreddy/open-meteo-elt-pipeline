# 🚀 Open Meteo ETL Pipeline (Airflow + AWS)

## 📌 Overview

This project demonstrates an end-to-end ETL pipeline using **Apache Airflow**, **Docker**, and **AWS S3**.

The pipeline:

* Extracts data from a public API
* Transforms it using Pandas
* Loads it into AWS S3

---

## 🏗️ Architecture

Airflow → Python (ETL) → AWS S3

---

## ⚙️ Tech Stack

* Apache Airflow
* Python (Pandas, Requests, Boto3)
* Docker
* AWS S3

---

## 🔄 Workflow

1. **Extract** → Fetch data from API
2. **Transform** → Clean & process data
3. **Load** → Upload to S3 bucket

---

## ▶️ How to Run

```bash
docker compose up -d
```

Open Airflow UI:

```
http://localhost:8080
```

---

## 🔐 Security

* AWS credentials handled via `.env`
* No secrets stored in code

---

## 📂 Project Structure

```
dags/
docker-compose.yaml
README.md
```

---

## 🚀 Future Improvements

* Add AWS Lambda trigger
* Add data validation
* Add monitoring & alerts

---

## 💼 Author

Aneesh Reddy
