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

cut = jieba.cut(text)
string = ' '.join(cut)
print(len(string))

img = Image.open('20210219161648629.png')  # 打开遮罩图片
img_array = np.array(img)  # 将图片转变成图片数组
wc = WordCloud(
    background_color='white',  # 形成的词云图片背景
    mask=img_array,  # 遮罩文件为数组
    font_path='msyhbd.ttc',  # 字体 所在位置为C:\Windows\Fonts
    stopwords='的'
)
wc.generate_from_text(string)  # 从文本中选择生成的词云对象

fig = plt.figure(1)  # 从第一个位置开始绘制
plt.imshow(wc)  # 按照词云wc的规则显示词云图片
plt.axis('off')  # 是否显示坐标轴

plt.show()

plt.savefig(r'.\static\assets\img\wordcloud.jpg', dpi=500)  # dpi=500 设置分别率
