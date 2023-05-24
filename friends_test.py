from pyspark.sql import HiveContext
import os
from backend.apps.service.friendrecommend.SparkSessionBase import SparkSessionBase
os.environ['JAVA_HOME'] = 'C:\Program Files\Java\jdk1.8.0_261'


class TextRandJob(SparkSessionBase):
    SPARK_URL = "local"
    SPARK_APP_NAME = 'TextRandJob'
    ENABLE_HIVE_SUPPORT = True

    def __init__(self):
        self.spark = self._create_spark_session()

    def start(self):
        id = 'TY6KFLkqqEbrQw_CRlR1bA'  #传入的用户id
        hc = HiveContext(self.spark.sparkContext)
        df_A = hc.table('review')
        df_B = hc.table('review')
        df_B.join(df_A, df_B['rev_business_id'] == df_A['rev_business_id'])\
        .where(df_B['rev_stars'] == df_A['rev_stars'])\
        .where(df_B['rev_user_id'] == id)\
        .where(df_B['rev_user_id'] != df_A['rev_user_id'])\
        .select(df_A['rev_user_id'])\
        .show()


if __name__ == '__main__':
    TextRandJob().start()
