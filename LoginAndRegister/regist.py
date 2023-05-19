from LoginAndRegister import check  ##引用正则判断脚本
from LoginAndRegister import storage  ##引用日志系统函数
from LoginAndRegister import main  ##引用菜单
from LoginAndRegister import db  ##引用数据库操作


def regist():
    username = input('请输入用户名：')
    if check.check_user(username) != True:
        storage.stor("system.log", f"用户名复杂度不符合要求，用户'{username}'注册失败")
        print('用户名只能是大小写字母或数字，且不能以数字开头，长度为5~12位')
        main.select()
    password = input('请输入密码：')
    if check.check_pwd(password) != True:
        storage.stor("system.log", f"密码复杂度不符合要求，用户'{username}'注册失败")
        print('密码必须且只能由大小写字母和数字组成，长度为6~15位：')
        main.select()
    ##实现用户体验感极好，哪里规则输错了，直接给提示，前面三个if判断，哪里不符合规则，直接返回主菜单重新走一遍
    ##并且将失败注册并记录进日志文件中。
    else:
        db.dml_insert(username, password)
    ##如果if全通过 直接 else，给他写入db文件，调用dml函数username，password，tel，insert插入数据库中。
    ##数据库有校验，如果有用户输入的用户，反之不让注册
