import os
import requests
from pyspark.sql import SparkSession
from pyspark.sql.functions import when, col
from pyspark.sql.types import StructType, StructField, IntegerType, StringType

LOG_FILE = "pyspark_output.md"

def log_output(operation, output, query=None):
    """Adds to a markdown file"""
    with open(LOG_FILE, "a") as file:
        file.write(f"The operation is {operation}\n\n")
        if query:
            file.write(f"The query is {query}\n\n")
        file.write("The truncated output is: \n\n")
        file.write(output)
        file.write("\n\n")

def start_spark(appName):
    spark = SparkSession.builder.appName(appName).getOrCreate()
    return spark

def end_spark(spark):
    spark.stop()
    return "stopped spark session"

def extract(
    url="https://raw.githubusercontent.com/fivethirtyeight/data/refs/heads/master/alcohol-consumption/drinks.csv",
    file_path="data/drinks.csv",
    directory="data",
):
    """Extract data from URL to a file path"""
    if not os.path.exists(directory):
        os.makedirs(directory)
    with requests.get(url) as r:
        with open(file_path, "wb") as f:
            f.write(r.content)
    return file_path

def load_data(spark, data="data/drinks.csv", name="Drinks"):
    """Load drinks.csv data"""
    # Schema based on the drinks.csv dataset
    schema = StructType([
        StructField("country", StringType(), True),
        StructField("beer_servings", IntegerType(), True),
        StructField("spirit_servings", IntegerType(), True),
        StructField("wine_servings", IntegerType(), True),
        StructField("total_litres_of_pure_alcohol", IntegerType(), True)
    ])

    df = spark.read.option("header", "true").schema(schema).csv(data)
    log_output("load data", df.limit(10).toPandas().to_markdown())

    return df

def query(spark, df, query, name): 
    """Queries using Spark SQL"""
    df.createOrReplaceTempView(name)
    result_df = spark.sql(query)
    log_output("query data", result_df.limit(10).toPandas().to_markdown(), query)
    return result_df.show()

def describe(df):
    summary_stats_str = df.describe().toPandas().to_markdown()
    log_output("describe data", summary_stats_str)
    return df.describe().show()

def example_transform(df):
    """Example transformation on the drinks dataset"""
    # Example: Categorizing countries based on beer servings
    df = df.withColumn(
        "alcohol_category",
        when(col("beer_servings") > 100, "High Beer")
        .when(col("beer_servings") > 50, "Moderate Beer")
        .otherwise("Low Beer")
    )
    log_output("transform data", df.limit(10).toPandas().to_markdown())
    return df.show()

