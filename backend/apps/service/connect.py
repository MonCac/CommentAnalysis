import pymysql as pymysql

con = pymysql.connect(host='192.168.102.130', port=3306, user='root', password='abx2002', database='yelp',
                      charset='utf8')