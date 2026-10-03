from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, IntegerType, StringType

# Task 1: Spark Setup & Data Loading

spark = SparkSession.builder \
    .master("local[2]") \
    .appName("SocialMediaSentiment_Task1") \
    .config("spark.driver.host", "127.0.0.1") \
    .config("spark.driver.bindAddress", "127.0.0.1") \
    .getOrCreate()

print("SparkSession created successfully!")

schema = StructType([
    StructField("id", IntegerType(), True),
    StructField("user", StringType(), True),
    StructField("text", StringType(), True),
    StructField("sentiment", StringType(), True)
])

df = spark.read.csv(
    "social_media.csv",
    header=True,
    schema=schema
)

print("CSV loaded successfully!")

print("First 5 rows:")
df.show(5, truncate=False)

print("DataFrame Schema:")
df.printSchema()

spark.stop()
