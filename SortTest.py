from pyspark.sql import HiveContext
from SparkSessionBase import SparkSessionBase
from pyspark.sql.functions import *


class TextRandJob(SparkSessionBase):
    SPARK_URL = "local"
    SPARK_APP_NAME = 'TextRandJob'
    ENABLE_HIVE_SUPPORT = True

    def __init__(self):
        self.spark = self._create_spark_session()

    def moren(self):
        hc = HiveContext(self.spark.sparkContext)
        b_df = hc.table('business')
        r_df = hc.table('review')

        # 连接生成新表
        new_df = b_df.join(r_df, b_df['business_id'] == r_df['rev_business_id']).distinct()

        # 默认排序
        new_df.withColumn("score", new_df['stars'] * 100 + new_df['review_count']) \
            .where(new_df['is_open'] == 1) \
            .select(col('name'), col('score')) \
            .orderBy(col('score').desc()).show()

    def choose(self, s):
        hc = HiveContext(self.spark.sparkContext)
        b_df = hc.table('business')
        # r_df = hc.table('review')

        # 连接生成新表
        new_df = b_df.distinct()

        # 默认排序
        new_df.withColumn("score", new_df['stars'] * 100 + new_df['review_count']) \
            .where(new_df['is_open'] == 1) \
            .select(col('name'), col(s)) \
            .orderBy(col(s).desc()).show()

    def choosecity(self,state,city):
        hc = HiveContext(self.spark.sparkContext)
        b_df = hc.table('business')
        # r_df = hc.table('review')

        # 连接生成新表
        new_df = b_df.distinct()

        # 默认排序
        new_df.withColumn("score", new_df['stars'] * 100 + new_df['review_count']) \
            .where(new_df['is_open'] == 1) \
            .where(col('state')==state)\
            .where(col('city')==city)\
            .select(col('name'), col(s)) \
            .orderBy(col(s).desc()).show()


# XXX 大数据分析代码

if __name__ == '__main__':
    # 点评推荐，距离，五星数量、评论数、平均分
    num = int(input("请选择您的筛选指标："))
    newlist = ['default', 'stars', 'review_count', '五星好评数', 'city and state']
    print(newlist[num])

    if num == 0:
        TextRandJob().moren()

    if num == 4:
        state = input("请输入州名：")
        city = input("请输入")

    else:
        TextRandJob().choose(newlist[num])





