# Stock Price Data Warehouse

## Overview

This project simulates a financial analytics pipeline for stock price data, inspired by real-world use cases like Barclays’ data engineering workflows. It builds a data warehouse using PySpark, PostgreSQL, DBT, and Apache Airflow. The pipeline automates the extraction, cleaning, enrichment, transformation, and storage of stock price data, enabling analysts and traders to derive actionable insights. 📊

---

## Problem Solved

Raw stock market data often contains missing or inconsistent values and lacks features for trend analysis or anomaly detection. This pipeline addresses these issues by:

* **Cleaning and validating** stock data.
* **Computing daily aggregates** (average price, total volume).
* **Adding features** like moving averages and anomaly flags for abnormal price changes.
* **Centralizing all data** in PostgreSQL for analytics and dashboarding.

---

## Features

### Data

* Synthetic dataset of **100K+ stock price records** with sequential daily prices.
* Includes `stock_id`, `date`, `price`, and `volume`.

### ETL Process

* **Extract:** Loads CSV or Parquet data using **PySpark**.
* **Transform:** Cleans and enriches data (moving averages, anomaly flags) using **PySpark** and **DBT**.
* **Load:** Stores results in a **PostgreSQL** data warehouse.

### Orchestration

* **Airflow DAG** automates the pipeline with logging and error handling.

### Scalability

* **Dockerized environment** ensures reproducibility and isolation.

### Advanced Features

* **7-day and 30-day moving averages** for trend analysis.
* **Daily anomaly detection** for sudden price spikes/drops (>10%).
* **Audit logs** for pipeline runs and data quality checks.

---

## Technologies

* **PySpark:** Efficient data extraction, cleaning, and enrichment.
* **PostgreSQL:** Reliable data warehousing and querying.
* **DBT:** SQL-based transformations and analytics-ready fact tables.
* **Apache Airflow:** Workflow orchestration and scheduling.
* **Docker:** Containerized environment for reproducibility.
* **Faker + Pandas:** Synthetic stock data generation for testing and development.

---

## Setup Instructions

### Prerequisites

* Docker and Docker Compose
* Python 3.9+
* PostgreSQL (local or Docker)
* Apache Airflow (local or Astronomer free tier)
* DBT (`pip install dbt-core dbt-postgres`)

### Steps

1.  **Clone repository**
    ```bash
    git clone [https://github.com/SanjeevikumarWD/stock-price-data-warehouse.git](https://github.com/SanjeevikumarWD/stock-price-data-warehouse.git)
    cd stock-price-data-warehouse
    ```

2.  **Build Docker image**
    ```bash
    docker build -t pyspark-etl -f docker/Dockerfile .
    ```

3.  **Start PostgreSQL**
    ```bash
    docker run -d --name postgres -e POSTGRES_PASSWORD=password -p 5432:5432 postgres
    ```

4.  **Initialize Airflow**
    ```bash
    pip install apache-airflow
    airflow db init
    airflow webserver --port 8080 &
    airflow scheduler
    ```

5.  **Copy DAG to Airflow**
    ```bash
    cp airflow/dags/stock_etl_dag.py ~/airflow/dags/
    ```

6.  **Initialize DBT**
    ```bash
    cd dbt
    dbt init --skip-profile-setup
    cp ../profiles.yml .
    ```

7.  **Run ETL**
    ```bash
    docker run --network host -v $(pwd)/data:/app/data -v $(pwd)/sql:/app/sql -v $(pwd)/dbt:/app/dbt pyspark-etl
    ```

---

## Access Results

* **Airflow UI:** http://localhost:8080
* **PostgreSQL:** `psql -h localhost -U postgres -d postgres`

---

## Results

* Processed **100K+ stock price records**.
* Created a fact table with:
    * `avg_price`
    * `total_volume`
    * 7-day & 30-day moving averages
    * `anomaly_flag` for sudden price changes
* Automated ETL pipeline with **Airflow and DBT**.
* Ready for BI dashboards or further machine learning pipelines. 🚀

---

## Learning Outcomes

* Hands-on experience with **PySpark, PostgreSQL, DBT, Airflow, and Docker**.
* Built a **production-grade financial analytics pipeline**.
* Learned **data cleaning, feature engineering, aggregation, anomaly detection, and orchestration**.
* Developed a **portfolio-ready project** simulating real-world investment analytics.

---

## Future Improvements

* Integrate **AWS S3** for scalable storage.
* Add data governance tools (e.g., **Alation**) for lineage and quality.
* Implement **incremental DBT models** for daily updates.
* Add **real-time streaming ingestion** with Kafka or Spark Structured Streaming.
* Enhance dashboarding using **Streamlit, PowerBI, or Metabase**.
