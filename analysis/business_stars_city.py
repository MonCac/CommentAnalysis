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

#统计评分最高的城市（前10）
        # b_df.select('name', 'city', 'stars') \
        #     .groupBy('city') \
        #     .agg(avg('stars').alias('avg_stars'), count('city').alias('count')) \
        #     .where(col('count') > 500) \
        #     .orderBy(col('avg_stars').desc()) \
        #     .limit(10)