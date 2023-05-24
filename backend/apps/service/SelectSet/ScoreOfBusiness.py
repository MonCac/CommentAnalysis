# 用户故事：我需要一个计算功能，根据数据信息将商家的优劣量化
#
# 描述：根据商家的距离远近，点评数量(business)，点评分数，以及结合用户打卡与评论的情况等，对商家进行综合性评分，用量化的数据评价不同商家对于用户的推荐程度，完成计算后可作为排序的标准。
#
# 验收准则：能够根据商家情况实际打分进行分析。
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
        # 读入数据
        hc = HiveContext(self.spark.sparkContext)
        b_df = hc.table('business')
        c_df = hc.table('checkin')
        r_df = hc.table('review')

        c_df = c_df.groupBy(col('business_id')).agg(count('checkin_dates').alias('打卡数'))
        r_df.where(col('rev_useful') == 1).groupBy(col('rev_business_id')).agg(avg('rev_stars').alias('平均分'))

        b_df = b_df.join(c_df, b_df['business_id'] == c_df['business_id'])

        new_b_df = b_df.join(r_df, b_df['business_id'] == r_df['rev_business_id'])

        # 加权得分（权值设置后期可修改）
        new_b_df.withColumn('score', new_b_df['stars'] + new_b_df['review_count'] + new_b_df['平均分'] + new_b_df['打卡数']) \
            .select(col('name'), col('score')) \
            .distinct() \
            .orderBy(col('score').desc()) \
            .show(1500, truncate=False)


if __name__ == '__main__':
    TextRandJob().start()
