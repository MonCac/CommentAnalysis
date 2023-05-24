from backend.apps.service.LoginAndRegister import db, main, storage, check


def login1():  # 改密码
    count = 0  ##定义个判断输错初始值
    for i in range(3):  # 限定三次范围
        username = input('请输入你的用户名：')
        password = input('请输入你的密码：')
        res = db.query(username)  ##请求一下数据库，看看有没有当前用户，锁定用户后面的用户信息也会跟着一起出来，结果res封装
        if password != res:  ##这里不判断用户名，因为即便你随便输入的用户名，查找对应的密码信息，如果没有此用户，里面也没有随便输入的用户名的密码信息。
            storage.stor("system.log", f"登录失败'{count + 1}'次")  ##将登录失败次数记录在log日志中
            print('登录失败')  ##给登录失败提示
            count += 1  ##失败一次直接给+1次
            if count == 3:  ##如果输错3次
                storage.stor("system.log", f"登录失败共'{count}'次")  ##统计次数记录日志中
                print('你已登录失败3次，请登录成功后再修改密码')  ##给提示
                main.select()  ##直接给他返回至主菜单页面
                count = 0  ##次数清零，解决下次循环出现报错清空
        else:
            count = 0
            storage.stor("system.log", f"用户'{username}'登录成功，")  ##否则直接登录成功，并记录日志，次数给归零
            newpassword = input('请输入你的新密码：')  ##输入新密码
            if check.check_pwd(newpassword) == True:  ##这里再次调用密码校验正则判断
                newwpassword = input('请再次输入你的新密码：')  ##再次输入一次密码，为了让用户输入密码别再忘了，用于用户新密码加深记忆
                if newpassword == newwpassword:  ##如果新输入的密码等于重新输入的新密码
                    db.dml_alter_pwd(newwpassword, username)  ##直接将重新输入的新密码写入数据库，并且指定哪个用户的新密码
                    storage.stor("system.log", f"用户‘{username}’修改密码成功")  ##写入日志某某修改成功
                    print('密码修改成功')  ##给修改成功提示
                    main.select()  ##返回主菜单页面
                else:  ##否则
                    storage.stor("system.log", f"2次输入的密码不一致，用户‘{username}’修改密码失败")  ##二次输入不一致，写入日志系统
                    print('2次输入的密码不一致，修改密码失败')  ##给用户提示
                    main.select()  ##直接回你老家吧，二次都失败了
            else:  ##大if的判断，如果你输入的新密码不符合复杂度
                storage.stor("system.log", "不符合密码复杂度要求，修改密码失败")  ##存入日志某某密码修改失败
                print('不符合密码复杂度要求，修改密码失败')  ##给用户提示
                main.select()  ##返回主菜单


def loginfo():  # 包括登录成功和登录失败三次
    count = 0  ##初始值给0
    for i in range(3):  ##3次失败范围
        username = input('请输入你的用户名：')
        password = input('请输入你的密码：')
        res = db.query(username)
        if password != res:
            storage.stor("system.log", f"登录失败'{count + 1}'次")
            print('登录失败')
            count += 1
            if count == 3:
                storage.stor("system.log", f"登录失败共'{count}'次")
                print('你已登录失败3次，返回主界面')
                main.select()
                count = 0
        else:
            storage.stor("system.log", f"用户‘{username}’登录成功")
            print('登陆成功')
            main.select()
            count = 0
# 整体思路如最上方一样，登录失败三次判断，记录日志，调用数据库用户信息数据，是否有。如果用户都写对，给他进入主菜单页面。
