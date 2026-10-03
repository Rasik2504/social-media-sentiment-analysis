SOCIAL MEDIA SENTIMENT SUMMARY - SPARK DATAFRAME PIPELINE

Files:
1. task1_spark_setup.py
   - Creates SparkSession
   - Loads social_media.csv with header and schema
   - Displays first 5 rows
   - Prints schema

2. task2_dataframe_transformations.py
   - select()
   - filter()
   - groupBy() + agg()
   - withColumn()

3. task3_sql_output.py
   - createOrReplaceTempView()
   - spark.sql()
   - Displays SQL results
   - Saves results as CSV and Parquet

Required:
- Python
- PySpark 4.2.0
- Java 17
- social_media.csv in the same folder as the Python files

Run:
python task1_spark_setup.py
python task2_dataframe_transformations.py
python task3_sql_output.py

The Task 3 script creates:
output/sentiment_summary_csv/
output/sentiment_summary_parquet/
