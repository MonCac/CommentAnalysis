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

    def start(self):
        id = 'qVc8ODYU5SZjKXVBgXdI7w'
        hc = HiveContext(self.spark.sparkContext)
        b_df = hc.table('users')
        list_common = b_df.where(col('user_id') == id).select('user_friends')
        list_common.show()



# XXX 大数据分析代码

if __name__ == '__main__':
    TextRandJob().start()
