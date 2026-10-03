from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, IntegerType, StringType

# ============================================
# TASK 3: SQL QUERY & OUTPUT
# ============================================

# 1. Create SparkSession
spark = SparkSession.builder \
    .master("local[2]") \
    .appName("SocialMediaSentiment_Task3") \
    .config("spark.driver.host", "127.0.0.1") \
    .config("spark.driver.bindAddress", "127.0.0.1") \
    .getOrCreate()

print("SparkSession created successfully!")

# ============================================
# 2. Define Schema
# ============================================

schema = StructType([
    StructField("id", IntegerType(), True),
    StructField("user", StringType(), True),
    StructField("text", StringType(), True),
    StructField("sentiment", StringType(), True)
])

# ============================================
# 3. Load CSV Dataset
# ============================================

df = spark.read.csv(
    "social_media.csv",
    header=True,
    schema=schema
)

print("CSV loaded successfully!")

# ============================================
# 4. Register DataFrame as Temporary View
# ============================================

df.createOrReplaceTempView("social_media")

print("Temporary view 'social_media' created successfully!")

# ============================================
# 5. SQL Query 1 - Positive Posts
# ============================================

positive_posts = spark.sql("""
    SELECT
        id,
        user,
        text,
        sentiment
    FROM social_media
    WHERE sentiment = 'positive'
""")

print("\nSQL QUERY 1 - Positive Posts:")
positive_posts.show(10, truncate=False)

# ============================================
# 6. SQL Query 2 - Sentiment Summary
# ============================================

sentiment_summary = spark.sql("""
    SELECT
        sentiment,
        COUNT(*) AS total_posts
    FROM social_media
    GROUP BY sentiment
    ORDER BY total_posts DESC
""")

print("\nSQL QUERY 2 - Sentiment Summary:")
sentiment_summary.show()

# ============================================
# 7. Save SQL Result as CSV
# ============================================
# Using Pandas here avoids the Windows Hadoop
# NativeIO problem encountered with Spark write.csv()

sentiment_summary.toPandas().to_csv(
    "sentiment_summary.csv",
    index=False
)

print("\nCSV output saved successfully!")
print("File: sentiment_summary.csv")

# ============================================
# 8. Stop Spark
# ============================================

spark.stop()

print("\nSparkSession stopped successfully!")
print("TASK 3 COMPLETED SUCCESSFULLY!")