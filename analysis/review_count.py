from SparkSessionBase import SparkSessionBase
from pyspark.sql import HiveContext
from pyspark.sql.functions import *
import os
os.environ['JAVA_HOME'] = 'C:\Program Files\Java\jdk1.8.0_261'


class TextRandJob(SparkSessionBase):
    SPARK_URL = "local"
    SPARK_APP_NAME = 'TextRandJob'
    ENABLE_HIVE_SUPPORT = True

    def __init__(self):
        self.spark = self._create_spark_session()

    # 用户故事：我需要一个每年总评论数统计功能，以至于我能统计总评论数
    # 描述：获取用户的评论数，将所有用户的评论数合并，得出总评论数量。统计要求：获取单个用户评论数，统计所有用户的评论总和
    # 验收准则：准确获得每年总评论数量
    def start(self):
        hcx = HiveContext(self.spark.sparkContext)

        df = hcx.table('review')

        result = df.select(col('review_id'), explode(split(col('rev_timestamp'), ',')).alias('datetime')) \
            .select('review_id', year(to_timestamp(trim(col('datetime')))).alias('year')) \
            .groupBy('year') \
            .count()

        result.show()

# XXX 大数据分析代码


if __name__ == '__main__':
    TextRandJob().start()
