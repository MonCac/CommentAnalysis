from pyspark.sql import HiveContext
from backend.apps.service.SparkSessionBase import SparkSessionBase
from pyspark.sql.functions import *
from backend.apps.service.SelectSet import DefaultSort


# 1. 添加排序功能，可根据点评推荐，距离，五星数量、评论数、平均分等条件进行排序，需要实现不同排序方式的功能。
# 2. 依据不同的排序要求，由优到劣展示数据，并且支持添加多个排序条件，依据默认优先级进行排序展示。
# 3. 如果未选择排序，则使用默认排序

class TextRandJob(SparkSessionBase):
    SPARK_URL = "local"
    SPARK_APP_NAME = 'TextRandJob'
    ENABLE_HIVE_SUPPORT = True

    def __init__(self):
        self.spark = self._create_spark_session()

    # 一个筛选指标，
    def choose(self, s):
        hc = HiveContext(self.spark.sparkContext)
        b_df = hc.table('business')
        r_df = hc.table('review')

        # 连接生成新表
        b_df = b_df.distinct()
        new_df = b_df.join(r_df, r_df['rev_business_id'] == b_df['business_id'])

        # 默认排序
        new_df.withColumn("五星数量", new_df['stars'] * 100 + new_df['review_count'])\
            .where(new_df['is_open'] == 1) \
            .select(col('name'), col(s)) \
            .orderBy(col(s).desc())\
            .show(1500, truncate=False)

    def choosecity(self, state, city):
        hc = HiveContext(self.spark.sparkContext)
        b_df = hc.table('business')
        # r_df = hc.table('review')

        # 连接生成新表
        new_df = b_df.distinct()

        # 默认排序
        new_df.where(new_df['is_open'] == 1) \
            .where(col('state') == state) \
            .where(col('city') == city) \
            .select(col('name'), col(s)) \
            .orderBy(col(s).desc()).show()


# XXX 大数据分析代码

if __name__ == '__main__':

    # 点评推荐，距离，五星数量、评论数、平均分
    num_choose = int(input("您有几个筛选指标："))
    num = int(input("请选择您的筛选指标："))
    newlist = ['default', 'stars', 'review_count', '五星好评数', 'city and state']
    print(newlist[num])

    if num == 0:
        DefaultSort.TextRandJob().start()

    if num == 4:
        state = input("请输入州名：")
        city = input("请输入")

    else:
        TextRandJob().choose(newlist[num])
