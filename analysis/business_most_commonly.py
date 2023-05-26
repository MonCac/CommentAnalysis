import os
os.environ['JAVA_HOME'] = 'C:\Program Files\Java\jdk1.8.0_261'

from pyspark import HiveContext
from pyspark.sql.functions import *
from backend.useless_file import SparkSessionBase

class TextRandJob(SparkSessionBase):
    SPARK_URL = "local"
    SPARK_APP_NAME = 'TextRandJob'
    ENABLE_HIVE_SUPPORT = True

    def __init__(self):
        self.spark = self._create_spark_session()


    def start(self):
        hc = HiveContext(self.spark.sparkContext)
        b_df = hc.table('business')
        r_df = hc.table('review')
        u_df = hc.table('users')
        c_df = hc.table('checkin')
        t_df = hc.table('tips')
#找出美国最常见商户（前20）
#找出美国最常见商户，并显示平均评分（前20）
        # b_df.select('name', 'stars') \
        #     .groupby('name') \
        #     .agg(avg(col('stars')).alias('avg_stars'),count('name').alias('count')) \
        #     .orderBy(col('count').desc())\
        #     .show(20)
