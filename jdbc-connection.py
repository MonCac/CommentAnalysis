import os
os.environ['JAVA_HOME'] = 'C:\Program Files\Java\jdk1.8.0_261'
from pyspark.sql import SparkSession
from pyspark import find_spark_home

spark = SparkSession \
    .builder \
    .master('local') \
    .appName('HelloSpark') \
    .getOrCreate()

df = spark.read.format("jdbc") \
    .option("url", "jdbc:mysql://192.168.102.130:3306/school") \
    .option("dbtable", "SC") \
    .option("user", "root") \
    .option("password", "abx2002") \
    .load()

df.printSchema()
df.show()