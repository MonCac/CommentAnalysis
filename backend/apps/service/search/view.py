from backend.apps.service.search import search
import pymysql

# 正常搜索
@search.route('/normalsearch')
def normalSearch(params):
    con = pymysql.connect(host='192.168.102.130', port=3306, user='root', password='abx2002', database='school',
                          charset='utf8')
    cursor = con.cursor()  # 游标做查询
    sql = f"select business_id, `name` from business where `name` like '%{params}%';"
    cursor.execute(sql)  # 查sql语句
    results = (cursor.fetchone())  # 封装查询结果，fetchone一条，固定写法
    cursor.close()
    con.close()
    return results


# 模糊搜索
@search.route('/fuzzysearch')
def fuzzySearch(params):
    con = pymysql.connect(host='192.168.102.130', port=3306, user='root', password='abx2002', database='school',
                          charset='utf8')
    cursor = con.cursor()  # 游标做查询
    sql = f"select business_id, `name` from business where categories like '%{params}%';"
    cursor.execute(sql)  # 查sql语句
    results = (cursor.fetchone())  # 封装查询结果，fetchone一条，固定写法
    cursor.close()
    con.close()
    return results