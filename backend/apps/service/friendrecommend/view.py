from backend.apps.service.friendrecommend import friendrecommend


# 相似商户评价推荐好友
@friendrecommend.route('/evaluationrecommendfriend')
def evaluationRecommendFriend(params):
    return


# 相似好友推荐好友
@friendrecommend.route('/friendrecommendfriend')
def friendRecommendFriend(params):
    return
