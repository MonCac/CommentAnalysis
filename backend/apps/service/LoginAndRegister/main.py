from backend.apps.service.LoginAndRegister import regist, login


# select函数


def select():
    print('*' * 46)  # 第一排46个星星
    print('*' * 7, 'Welcome To jira Info System', '*' * 7)
    print('*' * 2, '用户注册-0', '*', '商户注册-1', '*','登录-2', '*', '返回-9', '*' * 2)
    print('*' * 46)
# 以此类推46、7、2、46各行星星数其他的是绘制菜单的字符串
# 定个变量flag将input里的值保存到flag里，是用户输入的，并给用户提示后面跟上
    flag = input('please input menu number:')
    if flag == '0':
        regist.regist_user()  # 用户注册
    elif flag == '1':  # 商户注册
        regist.regist_shop()
    elif flag == '2':  # 登录
        login.login()
    elif flag == '9':
        exit('bye~')
    # 乱输入退出程序
    else:
        exit('input error~')


if __name__ == '__main__':
    select()
