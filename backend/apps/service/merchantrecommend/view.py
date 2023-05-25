from backend.apps.service.merchantrecommend import merchantrecommend


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
def recommendDefault(params):
    return


# 选择推荐方式
@merchantrecommend.route('/recommendbychoice')
def recommendByChoice(params):
    return


# 量化排序推荐
@merchantrecommend.route('/recommendbyquantization')
def recommendByQuantization(params):
    return


# 个性化推荐
@merchantrecommend.route('/recommendPersonalized')
def recommendPersonalized(params):
    return
