import os
os.environ['JAVA_HOME'] = 'C:\Program Files\Java\jdk1.8.0_261'

from pyspark import HiveContext
from pyspark.sql.functions import *
from backend.useless_file import SparkSessionBase

class TextRandJob(SparkSessionBase):
    SPARK_URL = "local"
    SPARK_APP_NAME = 'TextRandJob'
    ENABLE_HIVE_SUPPORT = True

    def __init__(self):
        self.spark = self._create_spark_session()


    def start(self):
        hc = HiveContext(self.spark.sparkContext)
        b_df = hc.table('business')
        r_df = hc.table('review')
        u_df = hc.table('users')
        c_df = hc.table('checkin')
        t_df = hc.table('tips')
#我需要一个优质用户数量统计功能，以至于我能统计出本年优质用户的数量，并且通过用户的数量对比得出优质用户的比例
#描述：获取用户的优质用户属性，统计优质用户的数量， 与总用户数量比对，得出优质用户比例。验收要求：
#验收准则：统计每年优质用户、普通用户比例
        u_df.join(r_df,u_df['user_id']==r_df['rev_user_id'])\
            .select('user_name','user_review_count',year(to_date('rev_Date')).alias('year'))\
            .groupBy('year','user_id')\
            .agg(count('*').alias('review_count'))
            .orderBy(col('user_review_count').desc()) \
            .show()
# 计算每个年份的总评论数和总评分
yearly_stats = r_df .groupBy(year(to_date('rev_Date')).alias('year')) \
    .agg(
        count("*").alias("total_reviews"),
    )

# 将每个评论所属的用户数据与每个评论的年份数据合并
            r_df.join(u_df, r_df["rev_user_id"] == u_df["user_id"]) \
                .select(year("rev_date").alias("year"), "user_id", "total_reviews", "total_rating")

# 计算每个年份的优质用户比例
yearly_user_stats = review_user_year \
    .groupBy("year") \
    .agg(
        sum(
            when(col("total_rating") / col("total_reviews") >= 4, 1)
        ).alias("good_users"),
        countDistinct("user_id").alias("total_users")
    ) \
    .withColumn("good_user_ratio", col("good_users") / col("total_users"))

yearly_user_stats.show()