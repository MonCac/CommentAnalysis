import pymysql
from flask import *
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
def recommendByChoice():
    params = request.args.get('recommendByChoice')
    params = str(params)
    con = pymysql.connect(host='192.168.102.130', port=3306, user='root', password='abx2002', database='yelp',
                          charset='utf8')
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


# 量化排序推荐
@merchantrecommend.route('/recommendbyquantization')
def recommendByQuantization():
    return recommendDefault()


# 个性化推荐
@merchantrecommend.route('/recommendPersonalized')
def recommendPersonalized(params):
    return
