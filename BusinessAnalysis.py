import os

os.environ['JAVA_HOME'] = '/Library/Java/JavaVirtualMachines/jdk-1.8.jdk/Contents/Home'

from pyspark import HiveContext
from SparkSessionBase import SparkSessionBase


class TextRandJob(SparkSessionBase):
    SPARK_URL = "local"
    SPARK_APP_NAME = 'TextRandJob'
    ENABLE_HIVE_SUPPORT = True

    def __init__(self):
        self.spark = self._create_spark_session()

    def start(self):
        hc = HiveContext(self.spark.sparkContext)
        b_df = hc.table('business')
        b_df.show()


# XXX 大数据分析代码

if __name__ == '__main__':
    TextRandJob().start()
