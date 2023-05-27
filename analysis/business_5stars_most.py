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
#五星评论最多的商户（20）
        # b_df.join(r_df,b_df['business_id'] == r_df['rev_business_id'])\
        #     .select(b_df['name'])\
        #     .where(r_df['rev_stars'] == 5) \
        #     .groupBy(b_df['name']) \
        #     .agg(count(b_df['name']).alias('count')) \
        #     .orderBy(col('count').desc())\
        #     .show(20)