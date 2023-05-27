import json

import pymysql
from flask import Blueprint, request

# 客户登录以及注册等基本功能
basefunction = Blueprint('basefunction', __name__)
print(22222)


@basefunction.route('/')
def hello():
    return 'hhhhh'

@basefunction.route('/userregister')
def userRegister():
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
    con = pymysql.connect(host='192.168.102.130', port=3306, user='root', password='abx2002', database='yelp',
                          charset='utf8')
    cursor = con.cursor()
    sql = f"insert into pwd(username,password,status) values('{username}','{password}', '{status}');"
    cursor.execute(sql)
    con.commit()
    return "注册成功"


# 登录
@basefunction.route('/login')
def login(params):
    username = params[0]
    password = params[1]
    con = pymysql.connect(host='192.168.102.130', port=3306, user='root', password='abx2002', database='yelp',
                          charset='utf8')
    cursor = con.cursor()  # 游标做查询
    sql = f"select password,status from pwd where username='{username}';"
    cursor.execute(sql)
    results = (cursor.fetchone())
    if results is None:  # 如果查询结果是空
        return (f"用户'{username}'不存在")
        cursor.close()
        con.close()
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



# 商户注册
@basefunction.route('/merchantregister')
def merchantRegister(params):
    username = params[0]
    password = params[1]
    status = 1
    con = pymysql.connect(host='192.168.102.130', port=3306, user='root', password='abx2002', database='yelp',
                          charset='utf8')
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
    con = pymysql.connect(host='192.168.102.130', port=3306, user='root', password='abx2002', database='yelp',
                          charset='utf8')
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
    con = pymysql.connect(host='192.168.102.130', port=3306, user='root', password='abx2002', database='yelp',
                          charset='utf8')
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
    con = pymysql.connect(host='192.168.102.130', port=3306, user='root', password='abx2002', database='yelp',
                          charset='utf8')
    cursor = con.cursor()
    sql = f"update business set address='{address}' where business_id='{business_id}';"
    cursor.execute(sql)
    con.commit()
    return "修改成功"

print(33333)

# 修改商户状态
@basefunction.route('/changemerchantstate')
def changeMerchantState(params):
    con = pymysql.connect(host='192.168.102.130', port=3306, user='root', password='abx2002', database='yelp',
                          charset='utf8')
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
    con = pymysql.connect(host='192.168.102.130', port=3306, user='root', password='abx2002', database='yelp',
                          charset='utf8')
    cursor = con.cursor()
    sql = f"update business set state='{state}',city='{city}' where business_id='{business_id}';"
    cursor.execute(sql)
    con.commit()
    return "修改成功"
