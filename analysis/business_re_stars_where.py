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
#统计不同类型（中国菜、美式、墨西哥）的餐厅的评分分布
        # b_df.select('stars', explode(split(col('Categories'), ', ')).alias('categories')) \
        #     .where(col('categories')== 'Mexican') \
        #     .groupby('stars') \
        #     .agg(count(col('stars')).alias('count')) \
        #     .orderBy(col('stars').asc())\
        #     .show()
        # b_df.select('stars', explode(split(col('Categories'), ', ')).alias('categories')) \
        #     .where(col('categories') == 'American') \
        #     .groupby('stars') \
        #     .agg(count(col('stars')).alias('count')) \
        #     .orderBy(col('stars').asc()) \
        #     .show()
        # b_df.select('stars', explode(split(col('Categories'), ', ')).alias('categories')) \
        #     .where(col('categories') == 'Chinese') \
        #     .groupby('stars') \
        #     .agg(count(col('stars')).alias('count')) \
        #     .orderBy(col('stars').asc()) \
        #     .show()