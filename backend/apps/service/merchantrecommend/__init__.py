import pymysql
from flask import *
from backend.apps.service.merchantrecommend import Filtrate0_Sort, Filtrate1_Sort, Filtrate2_Sort
from backend.apps.service.connect import dataConnect
# 推荐好友功能

merchantrecommend = Blueprint('merchantrecommend', __name__)


# 根据state推荐商家
@merchantrecommend.route('/recommendbystate')
def recommendByState():
    con = dataConnect()
    params = request.args.get('recommendByState')
    params = str(params)
    cursor = con.cursor()  # 游标做查询
    sql = f"select business_id,`name`, stars, address ,(stars * 2000 + review_count * 0.05) AS score " \
        f"FROM  business where is_open =1 AND state = '{params}'    order by score DESC LIMIT 12 "
    cursor.execute(sql)  # 查sql语句
    cursor.close()
    con.close()

    results = cursor.fetchall()  # 封装查询结果，fetchone一条，固定写法
    key = ('business_id', 'name', 'stars', 'address', 'score')
    resultList = []
    for row in results:
        resultList.append(dict(zip(key, row)))
    return resultList

# 根据city推荐商家
@merchantrecommend.route('/recommendbycity')
def recommendByCity():
    con = dataConnect()
    params = request.args.get('recommendByCity')
    params = str(params)
    cursor = con.cursor()  # 游标做查询
    sql = f"select business_id,`name`, stars, address ,(stars * 2000 + review_count * 0.05) AS score " \
        f"FROM  business where is_open =1 AND city = '{params}' order by score  DESC LIMIT 12 "
    cursor.execute(sql)  # 查sql语句
    cursor.close()
    con.close()

    results = cursor.fetchall()  # 封装查询结果，fetchone一条，固定写法
    key = ('business_id', 'name', 'stars', 'address', 'score')
    resultList = []
    for row in results:
        resultList.append(dict(zip(key, row)))
    print(resultList)
    return resultList

# 根据state和city推荐商家
@merchantrecommend.route('/recommendbystateandcity')
def recommendByStateAndCity():
    con = dataConnect()
    params = request.args.get('recommendByStateAndCity')
    params = str(params)
    json_obj = json.loads(params)
    state = json_obj['state']
    city = json_obj['city']

    cursor = con.cursor()  # 游标做查询
    sql = f"select business_id,`name`, stars, address ,(stars * 2000 + review_count * 0.05) AS score " \
        f"FROM  business where is_open =1 AND state = '{state}'AND city = '{city}' order by score DESC LIMIT 12 "
    cursor.execute(sql)  # 查sql语句
    cursor.close()
    con.close()

    results = cursor.fetchall()  # 封装查询结果，fetchone一条，固定写法
    key = ('business_id', 'name', 'stars', 'address', 'score')
    resultList = []
    for row in results:
        resultList.append(dict(zip(key, row)))
        print(resultList)
    return resultList


# # 默认推荐排序
# @merchantrecommend.route('/recommenddefault')
# def recommendDefault():
#     con = pymysql.connect(host='192.168.102.130', port=3306, user='root', password='abx2002', database='yelp',
#                           charset='utf8')
#     cursor = con.cursor()  # 游标做查询
#     sql = f"SELECT `name`, (stars * 100 + review_count) AS score " \
#         f"FROM business WHERE is_open = 1 ORDER BY score DESC LIMIT 1500;"
#
#     cursor.execute(sql)  # 查sql语句
#     results = cursor.fetchall()  # 封装查询结果，fetchone一条，固定写法
#     cursor.close()
#     con.close()
#
#     return results


# 选择推荐方式
@merchantrecommend.route('/recommendbychoice')
def recommendByChoice():
    con = dataConnect()
    params = request.args.get('recommendByChoice')
    params = str(params)
    cursor = con.cursor()  # 游标做查询
    sql = f"select business_id,`name`, stars, address ,(stars * 2000 + review_count * 0.05) AS score   " \
        f"FROM  business where is_open =1  order by {params} DESC LIMIT 12 "
    cursor.execute(sql)  # 查sql语句
    cursor.close()
    con.close()
    results = cursor.fetchall()  # 封装查询结果，fetchone一条，固定写法
    key = ('business_id', 'name', 'stars', 'address', 'score')
    resultList = []
    for row in results:
        resultList.append(dict(zip(key, row)))

    return resultList


# # 量化排序推荐
# @merchantrecommend.route('/recommendbyquantization')
# def recommendByQuantization():
#     return recommendDefault()
#
#
# # 个性化推荐
# @merchantrecommend.route('/recommendPersonalized')
# def recommendPersonalized(params):
#     return
