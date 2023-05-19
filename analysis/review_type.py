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

    # 用户故事：我需要评论类别统计功能，以至于我能统计出有用、有趣以及酷三种评论的数量
    # 描述：获取用户的评论的标签，分别将评论归于有用、有趣和酷三类。分类完成后统计各类评论的数量。验收要求：将评论分别置于三种评论类别中，统计各类评论数量
    # 验收准则：将评论分别置于三种评论类别中，统计各类评论数量
    def start(self):
        hcx = HiveContext(self.spark.sparkContext)
        df = hcx.table('review')
        result_useful = df.where(col('rev_useful') != 0) \
            .count()
        result_cool = df.where(col('rev_cool') != 0) \
            .count()
        result_funny = df.where(col('rev_funny') != 0) \
            .count()

        rdd = self.spark.sparkContext.parallelize(
            [('useful', result_useful), ('cool', result_cool), ('funny', result_funny)])
        df = rdd.toDF(['type', 'count'])

        df.show()

# XXX 大数据分析代码


if __name__ == '__main__':
    TextRandJob().start()
