import pymysql
from flask import Blueprint, request
from backend.apps.service.connect import dataConnect
# 推荐好友功能

search = Blueprint('search', __name__)


@search.route('/normalsearch')
def normalSearch():
    con = dataConnect()
    params = request.args.get("search")
    params = str(params)
    cursor = con.cursor()  # 游标做查询
    sql = f"select  business_id,`name`,categories,address from business where `name` like '%{params}%' and is_open=1 order by stars DESC,review_count DESC limit 10;"
    cursor.execute(sql)  # 查sql语句
    cursor.close()
    con.close()
    results = cursor.fetchall()  # 封装查询结果，fetchone一条，固定写法
    key = ("business_id","name","categories","address")
    resultList = []
    for row in results:
        resultList.append(dict(zip(key, row)))
    return resultList

# 模糊搜索
@search.route('/fuzzysearch')
def fuzzySearch():
    con = dataConnect()
    params = request.args.get("submit1")
    params = str(params)
    cursor = con.cursor()  # 游标做查询
    sql = f"select business_id,`name`,categories,address from business where categories like '%{params}%' order by stars,review_count limit 10;"
    cursor.execute(sql)  # 查sql语句
    results = (cursor.fetchall())  # 封装查询结果，fetchone一条，固定写法
    cursor.close()
    con.close()
    key = ("business_id", "name", "categories", "address")
    resultList = []
    for row in results:
        resultList.append(dict(zip(key, row)))
    print(resultList)
    return resultList

@search.route('/showinfo')
def showInfo():
    con = dataConnect()
    params = request.args.get("showShopInfo")
    params = str(params)
    print(params)
    cursor = con.cursor()  # 游标做查询
    sql = f"select  business_id,`name`,address,city,state,stars,review_count,is_open,attributes,categories,hours from business where business_id='{params}';"
    cursor.execute(sql)  # 查sql语句
    cursor.close()
    con.close()
    results = cursor.fetchall()  # 封装查询结果，fetchone一条，固定写法
    print(results)
    key = ("business_id","name","address","city","state","stars","review_count","is_open","attributes","categories","hours")
    resultList = []
    for row in results:
        resultList.append(dict(zip(key, row)))
    print(resultList)
    return resultList
