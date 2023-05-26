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
# 验收准则：不遗漏任何本年注册的新用户，不额外算入不在本年注册的新用户。
#         u_df.select(year(to_date('user_yelping_since')).alias('year')) \
#             .groupBy('year') \
#             .agg(count(col('year')).alias('count')) \
#             .orderBy(col('year').asc())\
#             .show()