from backend.apps.service.modify import modifypwd, modifyinfo


def select():
    print('*' * 2, '修改密码-0', '*', '商家信息修改-1', '*', '*' * 2)
# 以此类推46、7、2、46各行星星数其他的是绘制菜单的字符串
# 定个变量flag将input里的值保存到flag里，是用户输入的，并给用户提示后面跟上
    flag = input('please input menu number:')
    if flag == '0':
        modifypwd.alter_pwd()   # 修改密码
    # elif flag == '1':  # 商户信息修改

    elif flag == '9':
        exit('bye~')
    # 乱输入退出程序
    else:
        exit('input error~')


if __name__ == '__main__':
    select()
