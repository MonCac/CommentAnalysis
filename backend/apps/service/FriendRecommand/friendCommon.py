from pyspark.sql import HiveContext
import os

from pyspark.sql.functions import *

from backend.apps.service.FriendRecommand.SparkSessionBase import SparkSessionBase
os.environ['JAVA_HOME'] = 'C:\Program Files\Java\jdk1.8.0_261'


class TextRandJob(SparkSessionBase):
    SPARK_URL = "local"
    SPARK_APP_NAME = 'TextRandJob'
    ENABLE_HIVE_SUPPORT = True

    def __init__(self):
        self.spark = self._create_spark_session()

    def start(self):
        hc = HiveContext(self.spark.sparkContext)
        id = 'qVc8ODYU5SZjKXVBgXdI7w'  # 传入id
        df = hc.table('users').select('user_id', 'user_friends')
        result1 = df.select(col('user_id'), col('user_friends'))
        result2 = df.select(explode(split(col('user_friends'), ', ')).alias('friend')) \
            .where(col('user_id') == id)
        result2.join(result1, result2['friend'] == result1['user_id']) \
            .select(result1['user_friends']) \
            .show()
        # result2.join(result1, result2['friend'] == result1['user_id']) \
        #     .select(result2['friend'], result1['user_friends']) \
        #     .show()


# XXX 大数据分析代码

if __name__ == '__main__':
    TextRandJob().start()

