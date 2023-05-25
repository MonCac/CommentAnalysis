from backend.apps.service.loginandregister import db, main,  check

# 1为商铺，0为用户
def regist_user():
    status = 0
    username = input('请输入用户名：')
    if check.check_user(username) != True:
        print('用户名只能是大小写字母或数字，且不能以数字开头，长度为5~30位')
        main.select()
    password = input('请输入密码：')
    if check.check_pwd(password) != True:
        print('密码必须且只能由大小写字母和数字组成，长度为5~30位：')
        main.select()
    else:
        db.dml_insert(username, password, status)


def regist_shop():
    status = 1
    username = input('请输入商户名：')
    if check.check_user(username) != True:
        print('商户名只能是大小写字母或数字，且不能以数字开头，长度为5~30位')
        main.select()
    password = input('请输入密码：')
    if check.check_pwd(password) != True:
        print('密码必须且只能由大小写字母和数字组成，长度为5~30位：')
        main.select()
    else:
        db.dml_insert(username, password, status)
