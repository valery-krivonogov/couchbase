# -*- coding: utf-8 -*-
from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("Couchbase Spark Connector Example")\
    .config("spark.jars", "spark-connector-assembly-3.5.2.jar")\
    .config("spark.couchbase.connectionString", "couchbase://127.0.0.1")\
    .config("spark.couchbase.username", "admin")\
    .config("spark.couchbase.password", "Art_12503")\
    .getOrCreate()

spark.sparkContext.setLogLevel("OFF")

def load_data (collection_name):
    print("Load collection: "+collection_name)
    df = spark.read.format("couchbase.query")\
    .option("bucket", "travel-sample")\
    .option("scope", "inventory")\
    .option("collection", collection_name)\
    .load()
    df = df.drop("__META_ID").drop("type")
    df.printSchema()
    if collection_name != "hotel":
        df.show()

for tbl in ["airline","airport", "hotel","landmark","route"]:
    load_data(tbl)
    
#spark.stop()

