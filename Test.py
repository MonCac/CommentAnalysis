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
        b_df = hc.table('review')
        c_df = hc.table('business')

        # 验收准则：准确获得拥有五星数量最多的商户
        # b_df.join(c_df, b_df['rev_business_id'] == c_df['business_id']) \
        #     .where(col('rev_stars') == 5) \
        #     .groupBy('name') \
        #     .agg(count('rev_stars').alias('五星好评数')) \
        #     .orderBy(col('五星好评数').desc())\
        #     .show()

        # 准确获取所有用户评分星级，统计所有用户的评分分布情况
        # b_df.groupBy('rev_stars')\
        #     .agg(count('rev_user_id').alias('评论人数'))\
        #     .orderBy(col('rev_stars'))\
        #     .show()

        # 准确获取所有商户的周一～周日的评分星级次数，统计所有商户的周一～周日评分次数情况

        b_df.join(c_df, b_df['rev_business_id'] == c_df['business_id'])\
            .groupBy(weekofyear('rev_date'),'name')\
            .agg(count('rev_stars'))\
            .orderBy(weekofyear('rev_date'))\
            .show(truncate=False)




# XXX 大数据分析代码

if __name__ == '__main__':
    TextRandJob().start()

