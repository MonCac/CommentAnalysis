import pymysql
from backend.apps.service.modify import main
from backend.apps.service.LoginAndRegister import db, check


def alter_pwd():  # 改密码
    username = input('请输入你的用户名：')
    password = input('请输入你的密码：')
    res = db.query(username)  # 请求一下数据库，看看有没有当前用户，锁定用户后面的用户信息也会跟着一起出来，结果res封装
    if password != res:  # 这里不判断用户名，因为即便你随便输入的用户名，查找对应的密码信息，如果没有此用户，里面也没有随便输入的用户名的密码信息。
        print('密码错误')  # 给登录失败提示
    else:
        newpassword = input('请输入你的新密码：')  # 输入新密码
        if check.check_pwd(newpassword):  # 这里再次调用密码校验正则判断
            newwpassword = input('请再次输入你的新密码：')  # 再次输入一次密码，为了让用户输入密码别再忘了，用于用户新密码加深记忆
            if newpassword == newwpassword:  # 如果新输入的密码等于重新输入的新密码
                dml_alter_pwd(newwpassword, username)  # 直接将重新输入的新密码写入数据库，并且指定哪个用户的新密码
                print('密码修改成功')
                main.select()  # 返回主菜单页面
            else:
                print('2次输入的密码不一致，修改密码失败')
                main.select()
        else:
            print('不符合密码复杂度要求，修改密码失败')
            main.select()


def dml_alter_pwd(password, username):  # 修改用户密码
    con = pymysql.connect(host='192.168.102.130', port=3306, user='root', password='abx2002', database='school',
                          charset='utf8')
    cursor = con.cursor()
    sql = f"update pwd set password='{password}' where username='{username}';"
    cursor.execute(sql)
    con.commit()
