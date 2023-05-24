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

    # 用户故事：我需要一个打卡位置统计功能，以至于我能统计出最受欢迎的城市
    # 描述：获取用户的打卡位置，统计打卡所属的城市，分别统计城市的打卡数量并排序。统计要求：将打卡位置分配到城市和商户中，统计城市的打卡数量并排序
    # 验收准则：准确得出最受欢迎的城市
    def start(self):
        hcx = HiveContext(self.spark.sparkContext)
        df = hcx.table('checkin')
        business_df = hcx.table('business')

        result = df.join(business_df, df['business_id'] == business_df['business_id']) \
            .select(business_df['city']) \
            .groupBy('city') \
            .agg(count('city').alias('cnt')) \
            .orderBy(col('cnt').desc())
        result.show()

# XXX 大数据分析代码


if __name__ == '__main__':
    TextRandJob().start()
