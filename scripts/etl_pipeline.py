from pyspark.sql import SparkSession
from pyspark.sql.functions import col
import psycopg2
import pandas as pd

# Initialize Spark
spark = SparkSession.builder \
    .appName("StockDataWarehouse") \
    .getOrCreate()

# Read data
df = spark.read.csv("data/stocks.csv", header=True, inferSchema=True)

# Transform: Clean and prepare for DBT
df_clean = df.dropna().filter(col("price") > 0)
df_pandas = df_clean.toPandas()

# Write to PostgreSQL
conn = psycopg2.connect(
    dbname="postgres",
    user="postgres",
    password="password",
    host="localhost",
    port="5432"
)
cursor = conn.cursor()
cursor.execute(open("sql/create_table.sql", "r").read())
df_pandas.to_sql("raw_stocks", conn, if_exists="replace", index=False)
conn.commit()
cursor.close()
conn.close()

print("ETL pipeline completed: Data written to PostgreSQL")
spark.stop()
