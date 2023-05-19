from pyspark.ml.classification import LogisticRegression
from pyspark.sql import HiveContext
from SparkSessionBase import SparkSessionBase
from pyspark.sql import SparkSession
from pyspark.sql.types import *
from pyspark.sql.functions import *


class TextRandJob(SparkSessionBase):
    SPARK_URL = "local"
    SPARK_APP_NAME = 'TextRandJob'
    ENABLE_HIVE_SUPPORT = True

    def __init__(self):
        self.spark = self._create_spark_session()

    def start(self):
        hc = HiveContext(self.spark.sparkContext)
        b_df = hc.table('business')


        # 连接
        new_b_df = b_df.distinct()

        # 加权
        new_b_df.withColumn("score", new_b_df['stars'] * 100 + new_b_df['review_count']) \
            .where(new_b_df['is_open'] == 1)\
            .select(col('name'), col('score'))\
            .orderBy(col('score').desc()).show()


# XXX 大数据分析代码

if __name__ == '__main__':
    TextRandJob().start()
