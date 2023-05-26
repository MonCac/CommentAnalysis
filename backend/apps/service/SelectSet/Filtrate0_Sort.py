from pyspark.sql import HiveContext
from backend.apps.service.SparkSessionBase import SparkSessionBase
from pyspark.sql.functions import *


# 1. 添加排序功能，可根据点评推荐(default)，距离(state , city)，五星数量（review）、评论数(business)、平均分(stars)等条件进行排序，需要实现不同排序方式的功能。
# 2. 依据不同的排序要求，由优到劣展示数据，并且支持添加多个排序条件，依据默认优先级进行排序展示。
# 3. 如果未选择排序，则使用默认排序

class Filtrate0Sort(SparkSessionBase):
    SPARK_URL = "local"
    SPARK_APP_NAME = 'TextRandJob'
    ENABLE_HIVE_SUPPORT = True

    def __init__(self):
        self.spark = self._create_spark_session()

    # (0,1)只有一个排序指标，且无筛选指标
    def choose_one(self, s):
        hc = HiveContext(self.spark.sparkContext)
        b_df = hc.table('business')
        r_df = hc.table('review')
        five_df = r_df.where(col('rev_stars') == 5) \
            .groupBy('rev_business_id') \
            .agg(count('rev_stars').alias('五星好评数')) \
            .orderBy(col('五星好评数').desc())

        # 连接生成新表
        b_df = b_df.withColumn("score", b_df['stars'] * 100 + b_df['review_count'])  # 默认排序指标
        new_df = b_df.join(five_df, b_df['business_id'] == five_df['rev_business_id'])

        # 排序
        new_df.where(new_df['is_open'] == 1) \
            .select(col('name'), col(s)) \
            .distinct() \
            .orderBy(col(s).desc(), col('score').desc()) \
            .show(1500, truncate=False)

    # (0,2)
    def choose_two(self, s1, s2):
        hc = HiveContext(self.spark.sparkContext)
        b_df = hc.table('business')
        r_df = hc.table('review')
        five_df = r_df.where(col('rev_stars') == 5) \
            .groupBy('rev_business_id') \
            .agg(count('rev_stars').alias('五星好评数')) \
            .orderBy(col('五星好评数').desc())

        # 连接生成新表
        b_df = b_df.withColumn("score", b_df['stars'] * 100 + b_df['review_count'])  # 默认排序指标
        new_df = b_df.join(five_df, b_df['business_id'] == five_df['rev_business_id'])

        # 排序
        new_df.where(new_df['is_open'] == 1) \
            .select(col('name'), col(s1), col(s2)) \
            .distinct() \
            .orderBy(col(s1).desc(), col(s2).desc(), col('score').desc()) \
            .show(1500, truncate=False)

    # (0,3)
    def choose_three(self, s1, s2, s3):
        hc = HiveContext(self.spark.sparkContext)
        b_df = hc.table('business')
        r_df = hc.table('review')
        five_df = r_df.where(col('rev_stars') == 5) \
            .groupBy('rev_business_id') \
            .agg(count('rev_stars').alias('五星好评数')) \
            .orderBy(col('五星好评数').desc())

        # 连接生成新表
        b_df = b_df.withColumn("score", b_df['stars'] * 100 + b_df['review_count'])  # 默认排序指标
        new_df = b_df.join(five_df, b_df['business_id'] == five_df['rev_business_id'])

        # 排序
        new_df.where(new_df['is_open'] == 1) \
            .select(col('name'), col(s1), col(s2), col(s3)) \
            .distinct() \
            .orderBy(col(s1).desc(), col(s2).desc(), col(s3).desc(), col('score').desc()) \
            .show(1500, truncate=False)
