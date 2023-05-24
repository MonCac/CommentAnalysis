from pyspark.sql import HiveContext
from backend.apps.service.SparkSessionBase import SparkSessionBase
from pyspark.sql.functions import *


class TextRandJob(SparkSessionBase):
    SPARK_URL = "local"
    SPARK_APP_NAME = 'TextRandJob'
    ENABLE_HIVE_SUPPORT = True

    def __init__(self):
        self.spark = self._create_spark_session()

    def start(self):
        hc = HiveContext(self.spark.sparkContext)
        # b_df = hc.table('business')
        r_df = hc.table('review')

        # b_df = b_df.where(col('is_open')==1)
        # new_df = b_df.join(r_df, b_df['business_id']==r_df['rev_business_id'])
        #
        r_df.withColumn('score', col('rev_stars') / 5)\
            .select(col('score'))\
            .distinct()\
            .orderBy(col('score').desc()).show()


# XXX 大数据分析代码

if __name__ == '__main__':
    TextRandJob().start()
