## Stock Price Data Warehouse

### Overview

This project builds a data warehouse for stock price data, simulating financial analytics for Barclays. It uses PySpark for data extraction, PostgreSQL for storage, DBT for transformations, and Apache Airflow for orchestration.

### Features





- Data: Synthetic dataset of 100K stock price records (columns: stock_id, date, price, volume).



- ETL Process:





- Extract: Loads CSV data using PySpark.



- Transform: Cleans data with PySpark and aggregates (avg_price, total_volume) using DBT.



- Load: Stores results in a PostgreSQL data warehouse.



- Orchestration: Airflow DAG automates the pipeline.



- Environment: Dockerized PySpark setup.

### Technologies





- PySpark: Data extraction and cleaning.



- PostgreSQL: Data warehousing.



- DBT: SQL-based transformations.



- Apache Airflow: Workflow orchestration.



- Docker: Containerized environment.

## Setup Instructions





### Prerequisites:





- Docker and Docker Compose



- Python 3.9+



- PostgreSQL (local or Docker)



- Apache Airflow (local or Astronomer free tier)



- DBT (pip install dbt-core dbt-postgres)



### Steps:
```bash
# Clone repository
git clone https://github.com/SanjeevikumarWD/stock-price-data-warehouse.git
cd stock-price-data-warehouse

# Build Docker image
docker build -t pyspark-etl -f docker/Dockerfile .

# Start PostgreSQL
docker run -d --name postgres -e POSTGRES_PASSWORD=password -p 5432:5432 postgres

# Initialize Airflow (local)
pip install apache-airflow
airflow db init
airflow webserver --port 8080 &
airflow scheduler &

# Copy DAG to Airflow
cp airflow/dags/stock_etl_dag.py ~/airflow/dags/

# Initialize DBT
cd dbt
dbt init --skip-profile-setup
cp ../profiles.yml .

# Run ETL
docker run --network host -v $(pwd)/data:/app/data -v $(pwd)/sql:/app/sql -v $(pwd)/dbt:/app/dbt pyspark-etl
```


### Access Results:





- View Airflow UI at http://localhost:8080.



- Query PostgreSQL: psql -h localhost -U postgres -d postgres.

### Results





- Processed 100K stock price records.



- Created a fact table with average price and total volume per stock, stored in PostgreSQL.



- Automated pipeline with Airflow and DBT.

### Learning Outcomes





- Mastered PySpark, DBT, PostgreSQL, and Airflow for data warehousing.



- Built a financial analytics pipeline relevant to Barclays' data engineering roles.

### Future Improvements





- Integrate AWS S3 for scalability.



- Add data governance tools like Alation.



Implement advanced DBT tests.
