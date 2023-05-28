import pymysql
from backend.apps.service.merchantrecommend import merchantrecommend, Filtrate2_Sort, Filtrate1_Sort, Filtrate0_Sort
from flask import request
from backend.apps.service.connect import con
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
    cursor = con.cursor()  # 游标做查询
    sql = f"SELECT business_id,`name`,address,stars, (stars * 100 + review_count) AS score " \
        f"FROM business WHERE is_open = 1 ORDER BY score DESC LIMIT 12;"

    cursor.execute(sql)  # 查sql语句
    results = cursor.fetchall()  # 封装查询结果，fetchone一条，固定写法
    cursor.close()
    con.close()

    return results


# 选择推荐方式
@merchantrecommend.route('/recommendbychoice')
def recommendByChoice():
    params = request.args.get('recommendByChoice')
    cursor = con.cursor()  # 游标做查询
    sql = f"select `name`, stars, address   " \
        f"FROM  business where is_open =1 order by {params} DESC LIMIT 12 "
    cursor.execute(sql)  # 查sql语句
    results = cursor.fetchall()  # 封装查询结果，fetchone一条，固定写法
    cursor.close()
    con.close()
    return results


# 量化排序推荐
@merchantrecommend.route('/recommendbyquantization')
def recommendByQuantization():
    cursor = con.cursor()  # 游标做查询
    sql = f"SELECT state  FROM business "

    cursor.execute(sql)  # 查sql语句
    results = cursor.fetchall()  # 封装查询结果，fetchone一条，固定写法
    cursor.close()
    con.close()

    return results


# 个性化推荐
@merchantrecommend.route('/recommendPersonalized')
def recommendPersonalized(params):
    return


if __name__ == '__main__':
    print(recommendDefault())
