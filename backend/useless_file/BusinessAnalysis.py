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

# xsm大数据分析代码

#验收准则：可以获取所有商户的类别属性并全部正确分类，能够统计商户类别的数量，能够对商户类别进行排序
#统计最多的category及数量（前10
        # b_df.select(explode(split(col('Categories'), ', ')).alias('Categories'))\
        #     .groupby(col('Categories')) \
        #     .agg(count(col('Categories')).alias('count'))\
        #     .orderBy(col('count').desc())\
        #     .show(10)

#统计category的数量
        # b_df.select(explode(split(col('categories'), ', ').alias('categories'))) \
        #     .distinct()\
        #     .count()\
        #     .show()


#用户故事：我需要一个商户位置统计功能，以至于我能统计商户分布最多的城市和州
#验收准则：对所有商户的位置进行分类，得到每个城市/州的商户数量并排序
#商户最多的前10个城市
        # b_df.select(col('city'))\
        #     .groupBy('city')\
        #     .agg(count(col('city')).alias('count'))\
        #     .orderBy(col('count').desc())\
        #     .show(10)
#商户最多的前5个州
        # b_df.select(col('state')) \
        #     .groupBy('state') \
        #     .agg(count(col('state')).alias('count')) \
        #     .orderBy(col('count').desc()) \
        #     .show(5)

#用户故事：我需要一个商户评分统计功能，以至于我能获得同一间商户的五星评分总数
#验收准则：：准确获取商户的评分，准确统计并计算同一种商户的五星评分数并成功显示在对该商户的评价中
#五星评论最多的商户（20）
        # b_df.join(r_df,b_df['business_id'] == r_df['rev_business_id'])\
        #     .select(b_df['name'])\
        #     .where(r_df['rev_stars'] == 5) \
        #     .groupBy(b_df['name']) \
        #     .agg(count(b_df['name']).alias('count')) \
        #     .orderBy(col('count').desc())\
        #     .show(20)

#用户故事：我需要一个城市评分功能，以至于我能获得一座城市的平均评分
#描述：按照商户评分，获取商户的评分，将根据商户位置统计功能，将同一城市的商户的评分整合得到他们的平均评分。
# 统计要求：获取商户的评分，对同一城市商户的评分取平均值并显示在对该城市的平均评分中
#验收准则：：准确获取商户的评分，准确统计并计算同一城市商户的平均评分并成功显示在对该类型的评价中
#统计评分最高的城市（前10）
        # b_df.select('name', 'city', 'stars') \
        #     .groupBy('city') \
        #     .agg(avg('stars').alias('avg_stars'), count('city').alias('count')) \
        #     .where(col('count') > 500) \
        #     .orderBy(col('avg_stars').desc()) \
        #     .limit(10)

#用户故事：我需要一个餐厅分类功能，以至于我能根据餐厅的属性将不同的餐厅进行分类
#描述：获取商户的类别，单独统计Restaurant类别的商户属性，将同类别的餐厅归类并排序。
#统计要求：统计所有的Restaurant类商户，并通过其菜品类别再次分类
#验收准则：准确统计所有的Restaurant类商户并根据餐厅菜品分类
# 统计不同类型（中国菜、美式、墨西哥）的餐厅类型及数量
#         b_df.select(explode(split(col('Categories'), ', ')).alias('categories')) \
#             .where(
#             col('categories').isin('American', 'Mexican', 'Italian', 'Japanese', 'Chinese', 'Thai', 'Mediterranean'
#                                    , 'French', 'Vietnamese', 'Greek', 'Indian', 'Korean', 'Hawaiian', 'African',
#                                    'Spanish', 'Middle_eastern')) \
#             .groupby('categories') \
#             .agg(count(col('categories')).alias('count')) \
#             .orderBy(col('count').desc())\
#             .show()
#统计不同类型（中国菜、美式、墨西哥）的餐厅的评论数量
        # b_df.select('review_count',explode(split(col('Categories'), ', ')).alias('categories')) \
        #     .where(
        #     col('categories').isin('American', 'Mexican', 'Italian', 'Japanese', 'Chinese', 'Thai', 'Mediterranean'
        #                            , 'French', 'Vietnamese', 'Greek', 'Indian', 'Korean', 'Hawaiian', 'African',
        #                            'Spanish', 'Middle_eastern')) \
        #     .groupby('categories') \
        #     .agg(sum(col('review_count')).alias('review_sum')) \
        #     .orderBy(col('review_sum').desc()) \
        #     .show()

#统计不同类型（中国菜、美式、墨西哥）的餐厅的评分分布
        # b_df.select('stars', explode(split(col('Categories'), ', ')).alias('categories')) \
        #     .where(col('categories')== 'Mexican') \
        #     .groupby('stars') \
        #     .agg(count(col('stars')).alias('count')) \
        #     .orderBy(col('stars').asc())\
        #     .show()
        # b_df.select('stars', explode(split(col('Categories'), ', ')).alias('categories')) \
        #     .where(col('categories') == 'American') \
        #     .groupby('stars') \
        #     .agg(count(col('stars')).alias('count')) \
        #     .orderBy(col('stars').asc()) \
        #     .show()
        # b_df.select('stars', explode(split(col('Categories'), ', ')).alias('categories')) \
        #     .where(col('categories') == 'Chinese') \
        #     .groupby('stars') \
        #     .agg(count(col('stars')).alias('count')) \
        #     .orderBy(col('stars').asc()) \
        #     .show()

#用户故事：我需要一个连锁商户统计功能，以至于我能获得统计连锁商户的数量并排序
#描述：按照商户名称，获取商户的名称信息，将根据商户名称统计相同名称的商户，将同名商户归类为连锁并统计连锁店的数量。
# 统计要求：获取商户的名称，对同一名称的商户归类，建立连锁店属性，统计连锁店数量并排序
#验收准则：：准确获取商户的名称，对同一名称的商户归类，建立连锁店属性，统计连锁店数量并排序
#找出美国最常见商户（前20）
#找出美国最常见商户，并显示平均评分（前20）
        # b_df.select('name', 'stars') \
        #     .groupby('name') \
        #     .agg(avg(col('stars')).alias('avg_stars'),count('name').alias('count')) \
        #     .orderBy(col('count').desc())\
        #     .show(20)

#用户故事：我需要一个是否营业告知功能，以至于我能将知道商户当前是否开业
#描述：按照商户is_open属性，获取商户的开业状态，将开业状态公告在界面中，
# 如果可以，设计自动化开业功能，即当前时间和营业时间对应时修改商户的开业状态，商户方也可以自定义开业状态
#验收准则：准确获取开业状态，成功公告开业状态


#用户故事：我需要一个营业时间分类功能，以至于我能将商户分类为不同时段的营业商户
#描述：按照商户的营业时间，获取商户的营业时间段，根据不同的时段分类为早、午、晚、凌晨四类商户。
# 统计要求：获取营业时间，将商户分为四类时间营业，每个商户可以同时在多类存在
#验收准则：准确获取营业时间，将商户分类到四种时段，每个商户可以同时在多类时段存在


#用户故事：我需要一个人气统计功能，以至于我能统计出每个用户的粉丝数并根据这个排序得出人气最高的用户
#描述：获取用户的粉丝数，单独统计每个用户的粉丝数， 根据粉丝数量排序，得到粉丝最多的用户
#验收准则：根据粉丝数量排序，得到粉丝最多的用户
        # u_df.select('user_name', 'user_fans') \
        #     .orderBy(col('user_fans').desc()) \
        #     .show(1)

#用户故事：我需要一个评论数量统计功能，以至于我能统计出每个用户的评论数并根据这个排序
#描述：获取用户的评论数，单独统计每个用户的评论数， 根据评论数量排序，选出评论多的人作为评论达人
#验收准则：根据评论数量排序，选出评论多的人作为评论达人
        # u_df.select('user_name', 'user_review_count') \
        #     .orderBy(col('user_review_count').desc()) \
        #     .show(20)

# 用户故事：我需要一个新用户数量统计功能，以至于我能统计每年加入的新用户数量
# 描述：从每年固定时间开始计算，在这一年内注册的新用户会纳入统计，每年会统计该年注册的新用户数量。
# 验收准则：不遗漏任何本年注册的新用户，不额外算入不在本年注册的新用户。
#         u_df.select(year(to_date('user_yelping_since')).alias('year')) \
#             .groupBy('year') \
#             .agg(count(col('year')).alias('count')) \
#             .orderBy(col('year').asc())\
#             .show()

#我需要一个优质用户数量统计功能，以至于我能统计出本年优质用户的数量，并且通过用户的数量对比得出优质用户的比例
#描述：获取用户的优质用户属性，统计优质用户的数量， 与总用户数量比对，得出优质用户比例。验收要求：
#验收准则：统计每年优质用户、普通用户比例

#用户故事：我需要一个每年沉默用户（未写评论）比例统计功能，以至于我能统计出沉默用户的比例
#描述：获取用户的评论数，将当年评论数为零的人统计出来，计算这类沉默用户和总用户的比例。
# 统计要求：获取用户本年评论数为零的用户并统计数量，与总用户比对得到比例
#验收准则：显示每年总用户数、沉默用户数（未写评论）的比例
        # u_df.join(r_df,u_df[user_id]==)
        #     .select(year(to_date('user_yelping_since')).alias('year')) \
        #     .groupBy('year') \
        #     .agg(count(col('year')).alias('count')) \
        #     .orderBy(col('year').asc()) \
        #     .show()

#统计出每年的新用户数、评论数、精英用户、tip数、打卡数.
#列出结果表格
#列出结果折线图
#阐述你对结果的洞察分析
#执行时间




if __name__ == '__main__':
    TextRandJob().start()