import pymysql


def alter_name():
    username = 'Pns2l4eNsfO8kk83dixA6A'  # 传入id
    name = 'Abby Rappoport, LAC, CMQ'  # 商户名称
    address = '1616 Chapala St, Ste 2'
    city = 'Santa Barbara'
    state = 'CA'
    postal_code = '93101'
    latitude = 34.426678
    longtitude = -119.7112
    is_open = 0
    attributes = '{"ByAppointmentOnly":"True"}'
    categories = 'Doctors, Traditional Chinese Medicine, Naturopathic/Holistic, Acupuncture, Health & Medical, Nutritionists'
    hours = ''

    con = pymysql.connect(host='192.168.102.130', port=3306, user='root', password='abx2002', database='school',
                          charset='utf8')
    cursor = con.cursor()
    sql = f"update busniess set name='{name}' where business_id='{username}';"
    cursor.execute(sql)
    con.commit()
