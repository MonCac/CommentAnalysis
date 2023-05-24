from backend.apps.service.SparkSessionBase import SparkSessionBase
from backend.apps.service.SelectSet import Filtrate0_Sort, Filtrate1_Sort, DefaultSort, Filtrate2_Sort


# 1. 添加排序功能，可根据点评推荐，距离，五星数量、评论数、平均分等条件进行排序，需要实现不同排序方式的功能。
# 2. 依据不同的排序要求，由优到劣展示数据，并且支持添加多个排序条件，依据默认优先级进行排序展示。
# 3. 如果未选择排序，则使用默认排序

class TextRandJob(SparkSessionBase):
    SPARK_URL = "local"
    SPARK_APP_NAME = 'TextRandJob'
    ENABLE_HIVE_SUPPORT = True

    def __init__(self):
        self.spark = self._create_spark_session()


# XXX 大数据分析代码

if __name__ == '__main__':

    # 点评推荐，距离，五星数量、评论数、平均分
    num_filtrate = int(input("您有几个筛选指标(0,1,2)："))
    num_sort = int(input("您有几个排序指标（0，1，2，3）："))
    sort_list = ['stars', 'review_count', '五星好评数']

    #    .agg(count('rev_stars').alias('五星好评数'), col('score').alias('score'),
    #         col('review_count').alias('review_count'), col('stars').alias('stars'),
    #         avg('rev_stars').alias('平均分')) \
    # \
    if num_filtrate == 0:
        if num_sort == 0:
            DefaultSort.TextRandJob().start()

        elif num_sort == 1:
            num1 = int(input("请输入您的排序指标['stars', 'review_count', '五星好评数']："))
            Filtrate0_Sort.Filtrate0Sort().choose_one(sort_list[num1])

        elif num_sort == 2:
            num1 = int(input("请输入您的排序指标['stars', 'review_count', '五星好评数']："))
            num2 = int(input("请输入您的排序指标['stars', 'review_count', '五星好评数']："))
            Filtrate0_Sort.Filtrate0Sort().choose_two(sort_list[num1], sort_list[num2])

        elif num_sort == 3:
            num1 = int(input("请输入您的排序指标['stars', 'review_count', '五星好评数']："))
            num2 = int(input("请输入您的排序指标['stars', 'review_count', '五星好评数']："))
            num3 = int(input("请输入您的排序指标['stars', 'review_count', '五星好评数']："))
            Filtrate0_Sort.Filtrate0Sort().choose_three(sort_list[num1], sort_list[num2], sort_list[num3])

    if num_filtrate == 1:
        state = str(input("输入state:"))
        if num_sort == 0:
            Filtrate1_Sort.Filtrate1Sort().choose_zero(state)

        elif num_sort == 1:
            num1 = int(input("请输入您的排序指标['stars', 'review_count', '五星好评数']："))
            Filtrate1_Sort.Filtrate1Sort().choose_one(state, sort_list[num1])

        elif num_sort == 2:
            num1 = int(input("请输入您的排序指标['stars', 'review_count', '五星好评数']："))
            num2 = int(input("请输入您的排序指标['stars', 'review_count', '五星好评数']："))
            Filtrate1_Sort.Filtrate1Sort().choose_two(state, sort_list[num1], sort_list[num2])

        elif num_sort == 3:
            num1 = int(input("请输入您的排序指标['stars', 'review_count', '五星好评数']："))
            num2 = int(input("请输入您的排序指标['stars', 'review_count', '五星好评数']："))
            num3 = int(input("请输入您的排序指标['stars', 'review_count', '五星好评数']："))
            Filtrate1_Sort.Filtrate1Sort().choose_three(state, sort_list[num1], sort_list[num2], sort_list[num3])

    if num_filtrate == 2:
        state = str(input("输入state:"))
        city = str(input("输入city:"))

        if num_sort == 0:
            Filtrate2_Sort.Filtrate2Sort().choose_zero(state, city)

        elif num_sort == 1:
            num1 = int(input("请输入您的排序指标['stars', 'review_count', '五星好评数']："))
            Filtrate2_Sort.Filtrate2Sort().choose_one(state, city, sort_list[num1])

        elif num_sort == 2:
            num1 = int(input("请输入您的排序指标['stars', 'review_count', '五星好评数']："))
            num2 = int(input("请输入您的排序指标['stars', 'review_count', '五星好评数']："))
            Filtrate2_Sort.Filtrate2Sort().choose_two(state, city, sort_list[num1], sort_list[num2])

        elif num_sort == 3:
            num1 = int(input("请输入您的排序指标['stars', 'review_count', '五星好评数']："))
            num2 = int(input("请输入您的排序指标['stars', 'review_count', '五星好评数']："))
            num3 = int(input("请输入您的排序指标['stars', 'review_count', '五星好评数']："))
            Filtrate2_Sort.Filtrate2Sort().choose_three(state, city, sort_list[num1], sort_list[num2], sort_list[num3])
