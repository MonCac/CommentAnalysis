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

    # 用户故事：我需要对用户评论数进行统计
    # 描述：获取用户的全部评论数，并根据评论数进行降序排列生成一个排行榜或表单
    # 验收准则：生成一个全部评论用户的排行榜
    def start(self):
        hcx = HiveContext(self.spark.sparkContext)
        df = hcx.table('review')
        user_df = hcx.table('users')

        result = df.join(user_df, df['rev_user_id'] == user_df['user_id']) \
            .select(user_df['user_id'], user_df['user_name']) \
            .groupBy('user_id', 'user_name') \
            .agg(count('user_id').alias('cnt')) \
            .orderBy(col('cnt').desc()) \
            .limit(20)
        result.show()

# XXX 大数据分析代码


if __name__ == '__main__':
    TextRandJob().start()
