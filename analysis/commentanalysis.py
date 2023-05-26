import os
os.environ['JAVA_HOME'] = 'C:\Program Files\Java\jdk1.8.0_261'


from pyspark import HiveContext
from pyspark.sql.functions import *
from analysis.SparkSessionBase import SparkSessionBase
import pandas


class TextRandJob(SparkSessionBase):
    SPARK_URL = "local"
    SPARK_APP_NAME = 'TextRandJob'
    ENABLE_HIVE_SUPPORT = True

    def __init__(self):
        self.spark = self._create_spark_session()

    def start(self):
        hc = HiveContext(self.spark.sparkContext)
        df = hc.table('review')
        df.toPandas().to_csv('C:\\Users\\Administrator\\PycharmProjects\\comment-analysis-08\\analysis\\output.txt')
if __name__ == '__main__':
    TextRandJob().start()