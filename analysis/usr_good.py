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

# 将 review 表和 user 表进行关联，获取每条评论对应的用户名和评论时间
r_u_df = r_df.join(u_df, r_df[rev_user_id] == u_df[user_id]) \
                  .select("review_id", "user_name", "rev_date")

# 将评论时间转换为年份
review_user_year_df = r_u_df.withColumn(year("rev_date".alias("year")))

# 统计每年的评论总数和优质用户数
yearly_review_count_df = review_user_year_df.groupBy("year")
                        .agg(countDistinct("review_id").alias("review_count"),countDistinct("user_name").alias("active_user_count"))
yearly_review_count_df.show()

# 计算每年的优质用户比例
yearly_review_count_ratio_df = yearly_review_count_df.withColumn("quality_ratio", col("active_user_count") / col("review_count"))
yearly_review_count_ratio_df.show()