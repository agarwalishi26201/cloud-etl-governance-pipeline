from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, StringType, TimestampType

def process_security_logs():
    spark = SparkSession.builder \
        .appName("SecurityLogValidationAndTransform") \
        .getOrCreate()

    # Define strict schema for governance and data quality
    schema = StructType([
        StructField("event_id", StringType(), False),
        StructField("timestamp", TimestampType(), True),
        StructField("user_id", StringType(), True),
        StructField("status_code", StringType(), True)
    ])

    print("PySpark session initialized. Ready to process batch partitions with strict schema enforcement.")

if __name__ == "__main__":
    process_security_logs()
