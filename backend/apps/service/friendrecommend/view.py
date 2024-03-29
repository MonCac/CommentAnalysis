import pymysql

from backend.apps.service.friendrecommend import friendrecommend
from backend.apps.service.connect import con

# 相似商户评价推荐好友
@friendrecommend.route('/evaluationrecommendfriend')
def evaluationRecommendFriend(params):
    user_id = params
    cursor = con.cursor()
    #包含用户姓名，但搜索速度较慢
    # sql = f" select user_name,a.rev_user_id from review a join review b on a.rev_business_id=b.rev_business_id" \
    #     f" join users u on user_id=a.rev_user_id where a.rev_stars=b.rev_stars and b.rev_user_id!=a.rev_user_id " \
    #     f" and b.rev_user_id='{user_id}'limit 10;"
    sql = f" select a.rev_user_id,a.business_id from review a join review b on a.rev_business_id=b.rev_business_id" \
        f" where a.rev_stars=b.rev_stars and b.rev_user_id!=a.rev_user_id " \
        f" and b.rev_user_id='{user_id}'limit 10;"
    cursor.execute(sql)
    results = (cursor.fetchall())
    return results


# # 相似好友推荐好友
# @friendrecommend.route('/friendrecommendfriend')
# def friendRecommendFriend(params):
#     user_id = params
#     cursor = con.cursor()
#     sql = f" select u.user_id,t.friend from users u LATERAL view explode(split(u.user_friends, ', ')) t as friend where user_id='{user_id}' ;"
#     cursor.execute(sql)
#     results = cursor.fetchall()
#     return results


