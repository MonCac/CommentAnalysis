from backend.apps.service.search import search
import pymysql
from backend.apps.service.connect import con

# 正常搜索
@search.route('/normalsearch')
def normalSearch(params):
    cursor = con.cursor()  # 游标做查询
    sql = f"select * from business where `name` like '%{params}%' order by stars,review_count limit 10;"
    cursor.execute(sql)  # 查sql语句
    results = (cursor.fetchall())  # 封装查询结果，fetchone一条，固定写法
    cursor.close()
    con.close()
    return results


@search.route('/show')
def show(params):
    cursor = con.cursor()  # 游标做查询
    sql = f"select * from business where business_id='{params}';"
    cursor.execute(sql)  # 查sql语句
    results = (cursor.fetchall())  # 封装查询结果，fetchone一条，固定写法
    cursor.close()
    con.close()
    return results

# 模糊搜索
@search.route('/fuzzysearch')
def fuzzySearch(params):
    cursor = con.cursor()  # 游标做查询
    sql = f"select * from business where categories like '%{params}%' order by stars,review_count limit 10;"
    cursor.execute(sql)  # 查sql语句
    results = (cursor.fetchall())  # 封装查询结果，fetchone一条，固定写法
    cursor.close()
    con.close()
    return results
