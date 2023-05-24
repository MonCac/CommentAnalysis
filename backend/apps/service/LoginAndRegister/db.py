import pymysql
from pymysql import IntegrityError  # 引用内置函数
from backend.apps.service.LoginAndRegister import main


def query(username):  # 查询，校验注册及登录
    con = pymysql.connect(host='192.168.102.130', port=3306, user='root', password='abx2002', database='school',
                          charset='utf8')
    cursor = con.cursor()  # 游标做查询
    sql = f"select password from pwd where username='{username}';"
    # 将sql语句参数化sql前面写个f里面的username给它用花括号参数化
    cursor.execute(sql)  # 查sql语句
    results = (cursor.fetchone())  # 封装查询结果，fetchone一条，固定写法
    if results is None:  # 如果查询结果是空
        print(f"用户'{username}'不存在")  ##直接打印它不存在
        # 关闭查询，关闭数据数据库连接。保证占用资源损耗减少
        cursor.close()
        con.close()
        main.select()  # 不存在的用户，直接给它返回至主菜单
    else:  # 否则的话一定是直接成功，将results返回值取下标0直接取出来
        resul = results[0]  # 取一条数据
        cursor.close()
        con.close()
        return resul  # 给个返回值


def dml_insert(username, password, status):  # 注册信息储存
    con = pymysql.connect(host='192.168.102.130', port=3306, user='root', password='abx2002', database='school',
                          charset='utf8')
    cursor = con.cursor()
    sql = f"insert into pwd(username,password,status) values('{username}','{password}', '{status}');"
    # 这里注册信息用了个python报错异常处理try/except
    try:
        cursor.execute(sql)  # 执行
    except IntegrityError as e:  # 将这条开头的报错信息as成e
        if 'Duplicate' in str(e):  # 如果Dup在e报错里面
            print('用户名重复，注册失败')  ##给用户提示

    else:  # 这里逻辑就简单了，如果里面没有用户传入的用户直接，else写数据库里
        con.commit()  # 直接提交
        print('注册成功')  # 提示成功

    finally:  # 不论啥结果，直接返回至菜单。
        main.select()
