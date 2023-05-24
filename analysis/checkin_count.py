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

    # 用户故事：我需要打卡次数统计功能，以至于我能获得每年打卡次数数据
    # 描述：获取用户的打卡情况，获得所有用户的打卡次数总和。统计要求：获取所有用户打卡次数，统计选定时间段所有用户的打卡次数总和
    # 验收准则：准确得到选定时间段所有用户的打卡次数总和
    def start(self):
        hcx = HiveContext(self.spark.sparkContext)

        df = hcx.table('checkin')

        result = df.select(col('business_id'), explode(split(col('checkin_dates'), ',')).alias('datetime')) \
            .select('business_id', year(to_timestamp(trim(col('datetime')))).alias('year')) \
            .groupBy('year') \
            .count()

        result.show()

# XXX 大数据分析代码


if __name__ == '__main__':
    TextRandJob().start()
