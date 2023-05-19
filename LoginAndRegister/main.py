from LoginAndRegister import regist, login,storage

# select函数


def select():
    print('*' * 46)  # 第一排46个星星
    print('*' * 7, 'Welcome To jira Info System', '*' * 7)
    print('*' * 2, '注册-0', '*', '登录-1', '*', '改密-2', '*', '返回-9', '*' * 2)
    print('*' * 46)
# 以此类推46、7、2、46各行星星数其他的是绘制菜单的字符串
# 定个变量flag将input里的值保存到flag里，是用户输入的，并给用户提示后面跟上
    flag = input('please input menu number:')

# if判断0就去调用注册的函数进行注册，否则1、2、3、9一次类推
# 否则用户输入其他数字，输入哪个去哪个
    if flag == '0':
        regist.regist()  # 注册
    elif flag == '1':  # 登录
        login.loginfo()
    elif flag == '2':  # 改密码
        login.login1()
    elif flag == '9':
        exit('bye~')
    # 乱输入退出程序
    else:
        storage.stor("system.log", "输入不符合规则，退出程序")
        exit('input error~')


if __name__ == '__main__':
    select()
