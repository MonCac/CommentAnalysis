import pymysql
from flask import Flask, request
# from backend.apps.service.search import search
# from backend.apps.service.suggestion import suggestion
# from backend.apps.service.friendrecommend import friendrecommend
# from backend.apps.service.merchantrecommend import merchantrecommend
# from backend.apps.service.loginandregister import basefunction

app = Flask(__name__)


@app.route('/api/userregister/')
def userRegister(params):
    print(111111)
    username = params[0]
    password = params[1]
    status = 0
    con = pymysql.connect(host='192.168.102.130', port=3306, user='root', password='abx2002', database='yelp',
                          charset='utf8')
    cursor = con.cursor()
    sql = f"insert into pwd(username,password,status) values('{username}','{password}', '{status}');"
    cursor.execute(sql)
    con.commit()
    return "注册成功"

#
# app.register_blueprint(suggestion)
# app.register_blueprint(search)
# app.register_blueprint(friendrecommend)
# app.register_blueprint(merchantrecommend)
# app.register_blueprint(basefunction)


if __name__ == '__main__':
    app.run()