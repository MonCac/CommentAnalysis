from wordcloud import WordCloud
from PIL import Image
import numpy as np

mask = np.array(Image.open("20210219161648629.png"))

f = open('test.txt', 'r', encoding='utf-8')
txt = f.read()
# f.close
wordcloud = WordCloud(background_color="white",
                      width=800,
                      height=600,
                      max_words=200,
                      max_font_size=80,
                      mask=mask,
                      contour_width=3,
                      contour_color='steelblue'
                      ).generate(txt)
wordcloud.to_file('Alice_词云图.png')
