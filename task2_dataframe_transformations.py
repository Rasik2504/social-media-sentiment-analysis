from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, IntegerType, StringType
from pyspark.sql.functions import length, count

# Task 2: DataFrame Transformations

spark = SparkSession.builder \
    .master("local[2]") \
    .appName("SocialMediaSentiment_Task2") \
    .config("spark.driver.host", "127.0.0.1") \
    .config("spark.driver.bindAddress", "127.0.0.1") \
    .getOrCreate()

schema = StructType([
    StructField("id", IntegerType(), True),
    StructField("user", StringType(), True),
    StructField("text", StringType(), True),
    StructField("sentiment", StringType(), True)
])

df = spark.read.csv("social_media.csv", header=True, schema=schema)

# 1. select() - choose specific columns
selected_df = df.select("user", "text", "sentiment")
print("SELECT - Selected columns:")
selected_df.show(5, truncate=False)

# 2. filter() - keep positive sentiment rows
filtered_df = df.filter(df.sentiment == "positive")
print("FILTER - Positive sentiment rows:")
filtered_df.show(5, truncate=False)

# 3. groupBy() + agg() - count records by sentiment
summary_df = df.groupBy("sentiment").agg(count("*").alias("total_posts"))
print("GROUP BY + AGG - Sentiment summary:")
summary_df.show()

# 4. withColumn() - add a new column containing text length
transformed_df = df.withColumn("text_length", length(df.text))
print("WITH COLUMN - Added text_length:")
transformed_df.show(5, truncate=False)

spark.stop()
