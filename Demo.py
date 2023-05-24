from hashlib import new

from pyspark.ml.clustering import KMeans

from pyspark.ml.feature import VectorAssembler, StandardScaler
from pyspark.mllib.clustering import KMeans
from pyspark.sql import HiveContext
from backend.apps.service.SparkSessionBase import SparkSessionBase


class TextRandJob(SparkSessionBase):
    SPARK_URL = "local"
    SPARK_APP_NAME = 'TextRandJob'
    ENABLE_HIVE_SUPPORT = True

    def __init__(self):
        self.spark = self._create_spark_session()

    def start(self):
        # hc = HiveContext(self.spark.sparkContext)
        # b_df = hc.table('business')
        #
        #
        # # 连接
        # new_b_df = b_df.distinct()
        #
        # # 加权
        # new_b_df.withColumn("score", new_b_df['stars'] * 100 + new_b_df['review_count']) \
        #     .where(new_b_df['is_open'] == 1)\
        #     .select(col('name'), col('score'))\
        #     .orderBy(col('score').desc()).show(1500, truncate=False)

        hc = HiveContext(self.spark.sparkContext)
        user_df = hc.table('users')

        assembler = VectorAssembler().setInputCols(['review_count', 'useful', 'funny', 'cool']).setOutputCol('features')
        user_feature_df = assembler.transform(user_df)

        # 使用上面所有的参数归一，这里选取的字段仅是示例
        scaler = StandardScaler(inputCol='features', outputCol='scaledFeatures', withStd=True, withMean=False)

        scalerModel = scaler.fit(user_feature_df)
        scaled_user_feature_df = scalerModel.transform(user_feature_df)

        kmeans = new
        KMeans() \
            .setK(7) \
            .setSeed(100) \
            .setMaxIter(2) \
            .setFeaturesCol('scaledFeatures') \
            .setPredictionCol('predict')

        model = kmeans.fit(scaled_user_feature_df)
        predicted = model.transform(scaledFeatures)


# XXX 大数据分析代码

if __name__ == '__main__':
    TextRandJob().start()
