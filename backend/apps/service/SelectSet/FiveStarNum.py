# 获取商户的评论，统计评论中五星评分的数量并对数量排序，得出拥有五星评分最多的商户。

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
        b_df = hc.table('review')
        c_df = hc.table('business')

        # 验收准则：准确获得拥有五星数量最多的商户

        b_df.join(c_df, b_df['rev_business_id'] == c_df['business_id']) \
            .where(col('rev_stars') == 5) \
            .groupBy('name') \
            .agg(count('rev_stars').alias('五星好评数')) \
            .orderBy(col('五星好评数').desc())\
            .show()


# XXX 大数据分析代码

if __name__ == '__main__':
    TextRandJob().start()
