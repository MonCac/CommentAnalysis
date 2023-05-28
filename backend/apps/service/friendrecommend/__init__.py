import pymysql
import json
from flask import Blueprint, request
from backend.apps.service.connect import dataConnect
# 推荐好友功能

friendrecommend = Blueprint('friendrecommend', __name__)



@friendrecommend.route('/evaluationrecommendfriend')
def evaluationRecommendFriend():
    con = dataConnect()
    params = request.args.get("friendRecommend")
    user_id = str(params)
    cursor = con.cursor()
    #包含用户姓名，但搜索速度较慢
    sql = f" select a.rev_user_id,user_name from review a join review b on a.rev_business_id=b.rev_business_id" \
        f" join users u on user_id=a.rev_user_id where a.rev_stars=b.rev_stars and b.rev_user_id!=a.rev_user_id " \
        f" and b.rev_user_id='{user_id}'limit 10;"
    # sql = f" select a.rev_user_id,a.business_id from review a join review b on a.rev_business_id=b.rev_business_id" \
    #     f" where a.rev_stars=b.rev_stars and b.rev_user_id!=a.rev_user_id " \
    #     f" and b.rev_user_id='{user_id}'limit 10;"
    cursor.execute(sql)
    results = cursor.fetchall()
    key = ("id", "name")
    resultList=[]
    for row in results:
         resultList.append(dict(zip(key, row)))
    return resultList


# # 相似好友推荐好友
# @friendrecommend.route('/friendrecommendfriend')
# def friendRecommendFriend(params):
#     user_id = params
#     con = pymysql.connect(host='192.168.102.130', port=3306, user='root', password='abx2002', database='yelp',
#                           charset='utf8')
#     cursor = con.cursor()
#     sql = f" select u.user_id,t.friend from users u LATERAL view explode(split(u.user_friends, ', ')) t as friend where user_id='{user_id}' ;"
#     cursor.execute(sql)
#     results = cursor.fetchall()
#     return results