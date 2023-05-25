from backend.apps.service.loginandregister import db, main, storage, check



def login():  # 包括登录成功和登录失败三次
        username = input('请输入你的用户名：')
        password = input('请输入你的密码：')
        res = db.query(username)
        if password != res:
            print('密码错误，登录失败')
            main.select()
        else:
            print('登陆成功')
            main.select()  # 用户主页
