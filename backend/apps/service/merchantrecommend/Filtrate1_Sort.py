import pymysql
from backend.apps.service.connect import dataConnect


def choose_zero(state):
    con = dataConnect()
    cursor = con.cursor()  # 游标做查询
    sql = f"select `name`,(stars * 100 + review_count) AS score " \
        f"FROM  business where is_open =1 AND state = '{state}' order by score LIMIT 10 "
    cursor.execute(sql)  # 查sql语句
    results = cursor.fetchall()  # 封装查询结果，fetchone一条，固定写法
    cursor.close()
    con.close()
    return results


def choose_one(state, param1):
    con = dataConnect()
    cursor = con.cursor()  # 游标做查询
    sql = f"select `name`,  {param1} " \
        f"FROM  business where is_open =1 AND business.state = '{state}' order by {param1} DESC LIMIT 10 "
    cursor.execute(sql)  # 查sql语句
    results = cursor.fetchall()  # 封装查询结果，fetchone一条，固定写法
    cursor.close()
    con.close()
    return results


def choose_two(state, param1, param2):
    con = dataConnect()
    cursor = con.cursor()  # 游标做查询
    sql = f"select `name`,  {param1} ,{param2} " \
        f"FROM  business where is_open =1 AND state = '{state}' order by {param1} DESC, {param2} DESC LIMIT 10 "
    cursor.execute(sql)  # 查sql语句
    results = cursor.fetchall()  # 封装查询结果，fetchone一条，固定写法
    cursor.close()
    con.close()
    return results
