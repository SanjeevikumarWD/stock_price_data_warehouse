from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime
# dag
with DAG(
    "stock_etl",
    start_date=datetime(2025, 5, 26),
    schedule_interval="@daily",
    catchup=False
) as dag:
    generate_data = BashOperator(
        task_id="generate_data",
        bash_command="python /app/scripts/generate_data.py"
    )
    run_etl = BashOperator(
        task_id="run_etl",
        bash_command="python /app/scripts/etl_pipeline.py"
    )
    run_dbt = BashOperator(
        task_id="run_dbt",
        bash_command="dbt run --project-dir /app/dbt"
    )
    generate_data >> run_etl >> run_dbt
