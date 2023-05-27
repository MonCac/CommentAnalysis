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
#统计不同类型（中国菜、美式、墨西哥）的餐厅的评论数量
        # b_df.select('review_count',explode(split(col('Categories'), ', ')).alias('categories')) \
        #     .where(
        #     col('categories').isin('American', 'Mexican', 'Italian', 'Japanese', 'Chinese', 'Thai', 'Mediterranean'
        #                            , 'French', 'Vietnamese', 'Greek', 'Indian', 'Korean', 'Hawaiian', 'African',
        #                            'Spanish', 'Middle_eastern')) \
        #     .groupby('categories') \
        #     .agg(sum(col('review_count')).alias('review_sum')) \
        #     .orderBy(col('review_sum').desc()) \
        #     .show()