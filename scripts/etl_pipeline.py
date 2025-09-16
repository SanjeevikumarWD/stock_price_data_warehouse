from pyspark.sql import SparkSession
from pyspark.sql.functions import col, avg, lag, when, to_date
from pyspark.sql.window import Window
import psycopg2
import pandas as pd
from sqlalchemy import create_engine

# ----------------------------
# Initialize Spark
# ----------------------------
spark = SparkSession.builder \
    .appName("StockDataWarehouse") \
    .getOrCreate()

# ----------------------------
# Step 1: Read data
# ----------------------------
df = spark.read.csv("data/stocks.csv", header=True, inferSchema=True)

# ----------------------------
# Step 2: Data Cleaning
# ----------------------------
df_clean = (
    df.dropna()
      .filter(col("price") > 0)
      .withColumn("date", to_date(col("date"), "yyyy-MM-dd"))
)

# ----------------------------
# Step 3: Feature Engineering
# ----------------------------
window_spec = Window.partitionBy("stock_id").orderBy("date")

df_enriched = (
    df_clean
    .withColumn("moving_avg_7", avg("price").over(window_spec.rowsBetween(-6, 0)))
    .withColumn("prev_price", lag("price").over(window_spec))
    .withColumn(
        "anomaly_flag",
        when((col("price") - col("prev_price")) / col("prev_price") > 0.1, 1).otherwise(0)
    )
    .drop("prev_price")  # not needed in final
)

# ----------------------------
# Step 4: Convert to Pandas
# ----------------------------
df_pandas = df_enriched.toPandas()

# ----------------------------
# Step 5: Write to PostgreSQL
# ----------------------------
engine = create_engine("postgresql+psycopg2://postgres:password@localhost:5432/postgres") #change accordingly

# Create table if not exists
with engine.connect() as conn:
    with open("sql/create_table.sql", "r") as f:
        conn.execute(f.read())

# Load data (replace = overwrite, append = incremental)
df_pandas.to_sql("raw_stocks", engine, if_exists="replace", index=False)

print("✅ ETL pipeline completed: Data written to PostgreSQL")

# ----------------------------
# Stop Spark
# ----------------------------
spark.stop()
