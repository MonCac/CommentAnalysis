import json

from flask import request

from backend.apps.service.loginandregister import basefunction
import pymysql
from backend.apps.service.connect import con


# 登录
@basefunction.route('/login')
def login(params):
    username = params[0]
    password = params[1]
    cursor = con.cursor()  # 游标做查询
    sql = f"select password,status from pwd where username='{username}';"
    cursor.execute(sql)
    results = (cursor.fetchone())
    if results is None:  # 如果查询结果是空
        cursor.close()
        con.close()
        return f"用户'{username}'不存在"
    else:
        cursor.close()
        con.close()
        if password == results[0]:
            if results[1] == 0:
                return "用户登录成功"
            else:
                return "商户登录成功"
        else:
            return "密码错误"


# 用户注册
@basefunction.route('/userregister')
def userRegister(params):
    print(111111)
    username = params[0]
    password = params[1]
    status = 0
    cursor = con.cursor()
    sql = f"insert into pwd(username,password,status) values('{username}','{password}', '{status}');"
    cursor.execute(sql)
    con.commit()
    return "注册成功"


# 商户注册
@basefunction.route('/merchantregister')
def merchantRegister(params):
    username = params[0]
    password = params[1]
    status = 1
    cursor = con.cursor()
    sql = f"insert into pwd(username,password,status) values('{username}','{password}', '{status}');"
    cursor.execute(sql)
    con.commit()
    return "注册成功"


# 修改密码
@basefunction.route('/changepassword')
def changePassword(params):
    password = params[1]
    username = params[0]
    cursor = con.cursor()
    sql = f"update pwd set password='{password}' where username='{username}';"
    cursor.execute(sql)
    con.commit()
    return "修改成功"


# 修改商户名称
@basefunction.route('/changemerchantname')
def changeMerchantName(params):
    business_id = params[0]
    name = params[1]
    cursor = con.cursor()
    sql = f"update business set `name`='{name}' where business_id='{business_id}';"
    cursor.execute(sql)
    con.commit()
    return "修改成功"


# 修改商户地址
@basefunction.route('/changemerchantaddress')
def changeMerchantAddress(params):
    business_id = params[0]
    address = params[1]
    cursor = con.cursor()
    sql = f"update business set address='{address}' where business_id='{business_id}';"
    cursor.execute(sql)
    con.commit()
    return "修改成功"


# 修改商户状态
@basefunction.route('/changemerchantstate')
def changeMerchantState(params):
    cursor = con.cursor()
    sql = f"update business set is_open=1-is_open where business_id='{params}';"
    cursor.execute(sql)
    con.commit()
    return "修改成功"


# 修改商户所在州和城市
@basefunction.route('/changemerchantcity')
def changeMerchantCity(params):
    business_id = params[0]
    state = params[1]
    city = params[2]
    cursor = con.cursor()
    sql = f"update business set state='{state}',city='{city}' where business_id='{business_id}';"
    cursor.execute(sql)
    con.commit()
    return "修改成功"

#显示是否营业
@basefunction.route('/isopen')
def isOpen(params):
    business_id = params[0]
    is_open = params[1]
    cursor = con.cursor()
    sql = f"select is_open from business where business_id='{business_id}';"
    cursor.execute(sql)
    con.commit()
    result = cursor.fetchone()
    if result:
        is_open = result[0]
        if is_open:
            print("正常营业")
        else:
            print("关门歇业")
    else:
        print("没有这个企业", business_id)

#营业时间
@basefunction.route('/businesshours')
def businessHours(params):
    business_id = params[0]
    hours = params[1]
    cursor = con.cursor()
    sql = f"select hours from business where business_id='{business_id}';"
    cursor.execute(sql)
    con.commit()
    result = cursor.fetchone()
    if result:
        is_open = result[0]
        if is_open:
            print("正常营业")
        else:
            print("关门歇业")
    else:
        print("没有这个企业", business_id)