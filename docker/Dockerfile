FROM apache/spark-py:latest

WORKDIR /app COPY requirements.txt . 
RUN pip install --no-cache-dir -r requirements.txt 
COPY scripts/ /app/scripts/ COPY sql/ /app/sql/ 
CMD ["python", "/app/scripts/etl_pipeline.py"]
