import pymysql
from flask import *

suggestion = Blueprint('suggestion', __name__)

suggestion = Blueprint('suggestion', __name__)


# 市场分析建议
# @suggestion.route('/marketanalysissuggestion')
# def marketAnalysisSuggestion(params):
#     con = pymysql.connect(host='192.168.102.130', port=3306, user='root', password='abx2002', database='yelp',
#                           charset='utf8')
#     cursor = con.cursor()  # 游标做查询
#
#     sql = f"select categories from business where business_id = '{params}'"
#     cursor.execute(sql)  # 查sql语句
#     results = cursor.fetchall()  # 封装查询结果，fetchone一条，固定写法
#     cursor.close()
#     con.close()
#
#     if results == ((None,),):
#         return "请补充categories信息"
#     else:
#         return userManagementSuggestion(params)


# 设施需求建议
@suggestion.route('/facilityrequirementssuggestion')
def facilityRequirementsSuggestion():
    params = request.args.get('facilityrequirementssuggestion')
    params = str(params)
    print(params)

    con = pymysql.connect(host='192.168.102.130', port=3306, user='root', password='abx2002', database='yelp',
                          charset='utf8')
    cursor = con.cursor()  # 游标做查询

    sql = f" select tips_timestamp,tips_text from  tips" \
        f" where  tips_business_id = '{params}' LIMIT 3"
    cursor.execute(sql)  # 查sql语句
    cursor.close()
    con.close()
    results = cursor.fetchall()  # 封装查询结果，fetchone一条，固定写法
    key = ('tips_timestamp', 'tips_text')
    resultList = []
    for row in results:
        resultList.append(dict(zip(key, row)))
    print(resultList)
    return resultList

# # 用户经营建议
# @suggestion.route('/usermanagementsuggestion')
# def userManagementSuggestion(params):
#     con = pymysql.connect(host='192.168.102.130', port=3306, user='root', password='abx2002', database='yelp',
#                           charset='utf8')
#     cursor = con.cursor()  # 游标做查询
#
#     sql = f" select tips.tips_text from business join tips" \
#         f" on  business.business_id = tips.tips_business_id " \
#         f"where business.business_id = '{params}'"
#     cursor.execute(sql)  # 查sql语句
#     results = cursor.fetchall()  # 封装查询结果，fetchone一条，固定写法
#     cursor.close()
#     con.close()
#
#     if results == ():
#         return "没有用户的建议"
#     else:
#         return results[0]
