import pymysql
from flask import Blueprint

from backend.apps.service.merchantrecommend import Filtrate0_Sort, Filtrate1_Sort, Filtrate2_Sort

# 推荐好友功能

merchantrecommend = Blueprint('merchantrecommend', __name__)

# 根据浏览推荐商家
@merchantrecommend.route('/recommendbybrowsing')
def recommendByBrowsing(params):
    return


# 根据位置推荐商家
@merchantrecommend.route('/recommendbyposition')
def recommendByPosition(params):
    return


# 默认推荐排序
@merchantrecommend.route('/recommenddefault')
def recommendDefault():
    con = pymysql.connect(host='192.168.102.130', port=3306, user='root', password='abx2002', database='yelp',
                          charset='utf8')
    cursor = con.cursor()  # 游标做查询
    sql = f"SELECT `name`, (stars * 100 + review_count) AS score " \
        f"FROM business WHERE is_open = 1 ORDER BY score DESC LIMIT 1500;"

    cursor.execute(sql)  # 查sql语句
    results = cursor.fetchall()  # 封装查询结果，fetchone一条，固定写法
    cursor.close()
    con.close()

    return results


# 选择推荐方式
@merchantrecommend.route('/recommendbychoice')
def recommendByChoice(params):
    num_filtrate = params
    num_sort = int(input("您有几个排序指标（0，1，2）："))

    if num_filtrate == 0:
        if num_sort == 0:
            return recommendDefault()

        elif num_sort == 1:
            param1 = str(input("请输入您的排序指标['stars', 'review_count']："))
            return Filtrate0_Sort.choose_one(param1)

        elif num_sort == 2:
            param1 = str(input("请输入您的排序指标['stars', 'review_count']："))
            param2 = str(input("请输入您的排序指标['stars', 'review_count']："))
            return Filtrate0_Sort.choose_two(param1, param2)
    if num_filtrate == 1:
        state = str(input("输入state:"))
        if num_sort == 0:
            return Filtrate1_Sort.choose_zero(state)

        elif num_sort == 1:
            param1 = str(input("请输入您的排序指标['stars', 'review_count']："))
            return Filtrate1_Sort.choose_one(state, param1)

        elif num_sort == 2:
            param1 = str(input("请输入您的排序指标['stars', 'review_count']："))
            param2 = str(input("请输入您的排序指标['stars', 'review_count']："))
            return Filtrate1_Sort.choose_two(state, param1, param2)

    if num_filtrate == 2:
        state = str(input("输入state:"))
        city = str(input("输入city:"))
        if num_sort == 0:
            return Filtrate2_Sort.choose_zero(state, city)

        elif num_sort == 1:
            param1 = str(input("请输入您的排序指标['stars', 'review_count']："))
            return Filtrate2_Sort.choose_one(state, city, param1)

        elif num_sort == 2:
            param1 = str(input("请输入您的排序指标['stars', 'review_count']："))
            param2 = str(input("请输入您的排序指标['stars', 'review_count']："))
            return Filtrate2_Sort.choose_two(state, city, param1, param2)


# 量化排序推荐
@merchantrecommend.route('/recommendbyquantization')
def recommendByQuantization():
    return recommendDefault()


# 个性化推荐
@merchantrecommend.route('/recommendPersonalized')
def recommendPersonalized(params):
    return

