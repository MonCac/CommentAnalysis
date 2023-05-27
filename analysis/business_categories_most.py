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

#验收准则：可以获取所有商户的类别属性并全部正确分类，能够统计商户类别的数量，能够对商户类别进行排序
#统计最多的category及数量（前10
        b_df.select(explode(split(col('Categories'), ', ')).alias('Categories'))\
            .groupby(col('Categories')) \
            .agg(count(col('Categories')).alias('count'))\
            .orderBy(col('count').desc())\
            .show(10)
