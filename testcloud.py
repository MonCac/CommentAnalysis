import jieba  # 分词
import pymysql
from PIL import Image  # 图片处理
from matplotlib import pyplot as plt  # 绘图 数据可视化
from wordcloud import WordCloud  # 词云
import numpy as np  # 矩阵运算
con = pymysql.connect(host='192.168.102.130', port=3306, user='root', password='abx2002', database='yelp',
                      charset='utf8')

cur = con.cursor()
sql = 'select rev_text from review'
data = cur.execute(sql)
text = ""
for item in data:
    text = text + item[0]  # 将所有文本拼接到一起
    # print(item[0])
cur.close()
con.close()

words = jieba.lcut(text)  # 精确分词
newtxt = ' '.join(words)  # 空格拼接
wordcloud = WordCloud(font_path="msyh.ttf").generate(newtxt)
wordcloud.to_file('词yun.jpg')
