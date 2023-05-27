import pymysql



def choose_one(paramss):
    con = pymysql.connect(host='192.168.102.130', port=3306, user='root', password='abx2002', database='yelp',
                          charset='utf8')
    cursor = con.cursor()  # 游标做查询
    sql = f"select `name`,  {paramss}  " \
        f"FROM  business where is_open =1 order by {paramss} DESC LIMIT 12 "
    cursor.execute(sql)  # 查sql语句
    results = cursor.fetchall()  # 封装查询结果，fetchone一条，固定写法
    cursor.close()
    con.close()
    return results


def choose_two(param1, param2):
    con = pymysql.connect(host='192.168.102.130', port=3306, user='root', password='abx2002', database='yelp',
                          charset='utf8')
    cursor = con.cursor()  # 游标做查询
    sql = f"select `name`,  {param1} ,{param2} " \
        f"FROM  business where is_open =1 order by {param1} DESC, {param2} DESC LIMIT 10 "
    cursor.execute(sql)  # 查sql语句
    results = cursor.fetchall()  # 封装查询结果，fetchone一条，固定写法
    cursor.close()
    con.close()
    return results


def test1():
    con = pymysql.connect(host='192.168.102.130', port=3306, user='root', password='abx2002', database='yelp',
                          charset='utf8')
    cursor = con.cursor()  # 游标做查询
    sql = f" SELECT * from business join " \
        f" (select rev_business_id, count(rev_business_id)as cnt from review where rev_stars = 5 group by rev_business_id)as rev_df" \
        f" on  business.business_id = rev_df.rev_business_id " \
        f" where is_open = 1 order by stars DESC LIMIT 10 "

    cursor.execute(sql)  # 查sql语句
    results = cursor.fetchall()  # 封装查询结果，fetchone一条，固定写法
    cursor.close()
    con.close()

    return results


def test2():
    con = pymysql.connect(host='192.168.102.130', port=3306, user='root', password='abx2002', database='yelp',
                          charset='utf8')
    cursor = con.cursor()  # 游标做查询

    sql = f"select rev_business_id, count(rev_business_id)as cnt from review where rev_stars = 5 " \
        f" group by rev_business_id  order by cnt DESC limit 10"

    cursor.execute(sql)  # 查sql语句
    results = cursor.fetchall()  # 封装查询结果，fetchone一条，固定写法
    cursor.close()
    con.close()
    return results


if __name__ == '__main__':
    print(test1())
