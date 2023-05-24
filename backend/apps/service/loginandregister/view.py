from backend.apps.service.loginandregister import basefunction


# 用户登录
@basefunction.route('/login')
def login(params):
    return


# 用户注册
@basefunction.route('/userregister')
def userRegister(params):
    return


# 商户注册
@basefunction.route('/merchantregister')
def merchantRegister(params):
    return


# 修改密码
@basefunction.route('/changepassword')
def changePassword(params):
    return


# 修改商户名称
@basefunction.route('/changemerchantname')
def changeMerchantName(params):
    return


# 修改商户地址
@basefunction.route('/changemerchantaddress')
def changeMerchantAddress(params):
    return


# 修改商户状态
@basefunction.route('/changemerchantstate')
def changeMerchantState(params):
    return


# 修改商户所在城市
@basefunction.route('/changemerchantcity')
def changeMerchantCity(params):
    return
