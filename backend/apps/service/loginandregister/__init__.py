import json

import pymysql
from flask import Blueprint, request
from backend.apps.service.connect import dataConnect
# 客户登录以及注册等基本功能
basefunction = Blueprint('basefunction', __name__)
print(22222)



@basefunction.route('/')
def hello():
    return 'hhhhh'


# 用户注册
@basefunction.route('/userregister')
def userRegister():
    con = dataConnect()
    print(111111)
    print(231)
    params = request.args.get("register")
    print(params)
    params = str(params)
    json_obj = json.loads(params)
    print(params)
    print(json_obj)
    print(2131)
    username = json_obj['username']
    print(username)
    password = json_obj['password']
    print(password)
    status = 0
    cursor = con.cursor()
    sql = f"insert into pwd(username,password,status) values('{username}','{password}', '{status}');"
    cursor.execute(sql)
    con.commit()
    return "注册成功"


# 登录
@basefunction.route('/login')
def login():
    con=dataConnect()
    status=0
    params = request.args.get("login")
    params = str(params)
    json_obj = json.loads(params)
    username = json_obj['username']
    password = json_obj['password']
    cursor = con.cursor()  # 游标做查询
    sql = f"select password,status from pwd where username='{username}';"
    cursor.execute(sql)
    results = cursor.fetchone()
    sql_business = f"select business_id from pwd where username='{username}';"
    cursor.execute(sql_business)
    result_business=cursor.fetchone()
    key = ("business_id")
    result_business=dict(zip(key, result_business))
    data=json.dumps(result_business)
    print(data)
    if results is None:  # 如果查询结果是空
        status=0  # 用户名不存在
    else:
        if password == results[0]:
            status=2  # 登录成功
        else:
            status=1  # 密码错误
    data=json.loads(data)
    data['status']=status
    result_business = json.dumps(data)
    print(result_business)
    return result_business



# 用户注册


# 商户注册
@basefunction.route('/merchantregister')
def merchantRegister():
    con = dataConnect()
    params = request.args.get("register")
    params = str(params)
    json_obj = json.loads(params)
    username = json_obj['username']
    password = json_obj['password']
    business_id=json_obj['business_id']
    status = 1
    cursor = con.cursor()
    sql = f"insert into pwd(username,password,status,business_id) values('{username}','{password}', '{status}','{business_id}');"
    cursor.execute(sql)
    con.commit()
    return "注册成功"


# 修改密码
@basefunction.route('/changepassword')
def changePassword(params):
    con = dataConnect()
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
    con = dataConnect()
    business_id = params[0]
    name = params[1]
    cursor = con.cursor()
    # sql = f"update business set `name`='{name}' where business_id='{business_id}';"
    # cursor.execute(sql)
    con.commit()
    return "修改成功"


# 修改商户地址
@basefunction.route('/changemerchantaddress')
def changeMerchantAddress():
    con = dataConnect()
    params=request.args.get("saveAddress")
    params = str(params)
    json_obj = json.loads(params)
    address = json_obj['address']
    business_id = json_obj['business_id']
    cursor = con.cursor()
    sql = f"update business set address='{address}' where business_id='{business_id}';"
    cursor.execute(sql)
    con.commit()
    return "修改成功"


# 修改商户状态
@basefunction.route('/changemerchantstate')
def changeMerchantState():
    con = dataConnect()
    params = request.args.get("saveGender")
    print(params)
    params = str(params)
    json_obj = json.loads(params)
    is_open = json_obj['status']
    print(is_open)
    business_id = json_obj['business_id']
    cursor = con.cursor()
    sql = f"update business set is_open=1-is_open where business_id='{business_id}';"
    cursor.execute(sql)
    con.commit()
    return "修改成功"


# 修改商户所在州和城市
@basefunction.route('/changemerchantcity')
def changeMerchantCity(params):
    con = dataConnect()
    business_id = params[0]
    state = params[1]
    city = params[2]
    cursor = con.cursor()
    sql = f"update business set state='{state}',city='{city}' where business_id='{business_id}';"
    cursor.execute(sql)
    con.commit()
    return "修改成功"
