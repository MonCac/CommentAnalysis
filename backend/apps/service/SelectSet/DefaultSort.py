# 根据是否营业>评价（打卡）数量>评分结果>地理位置的标准对商家进行排序

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

        # 去重
        new_b_df = b_df.distinct()

        # 加权得分（权值设置后期可修改）
        new_b_df.withColumn("score", new_b_df['stars'] * 100 + new_b_df['review_count']) \
            .where(new_b_df['is_open'] == 1) \
            .select(col('name'), col('score')) \
            .orderBy(col('score').desc()).show(1500, truncate=False)
