import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from wordcloud import ImageColorGenerator

plt.rc('font', family='AppleGothic')

class Visualization:
    def __init__(self, wordList):
        self.wordList = wordList
        self.wordDict = dict(wordList)
    # end def __init__(self, wordList)

    def makeWordCloud(self):
        alice_color_file = './../04.wordcloud/alice_color.png'
        alice_coloring = np.array(Image.open(alice_color_file))

        fontpath = 'AppleGothic'
        wordcloud = WordCloud(font_path=fontpath, mask=alice_coloring,
                              relative_scaling=0.2, background_color='lightyellow')

        wordcloud = wordcloud.generate_from_frequencies(self.wordDict)

        image_colors = ImageColorGenerator(alice_coloring)

        wordcloud = wordcloud.recolor(color_func=image_colors, random_state=42)

        plt.imshow(wordcloud)
        plt.axis('off')

        filename = 'myWordCloud.png'
        plt.savefig(filename, dpi=400)
        print(filename + '파일 저장됨')
    # end def makeWordCloud(self)

    def makeBarChart(self):
        plt.figure(figsize=(12, 8))
        barcount = 10
        result = self.wordList[:barcount]

        chartdata = [] # 차트 수치
        xdata = [] # 글씨

        for idx in range(len(result)):
            chartdata.append(result[idx][1])
            xdata.append(result[idx][0])

            value = str(chartdata[idx]) + '건' # 예시 : 60건

            plt.text(x=idx, y=chartdata[idx]-5, s=value,
                     fontsize=12, horizontalalignment='center')

        mycolor = ['r','g','b','y','m','c','#FFCC00','#CCFFBB','#05CCFF','#11CCFF']
        plt.bar(range(barcount), chartdata, align='center', color=mycolor)
        plt.xticks(range(barcount), xdata, rotation=45)

        plt.title('상위 ' + str(barcount) + '빈도 수')

        xlow, xhigh = -0.5, barcount -0.5

        plt.xlim([xlow, xhigh])
        plt.ylim([0, 50])
        plt.xlabel('주요 키워드')
        plt.ylabel('빈도수')

        filename = 'myBarChart.png'
        plt.savefig(filename, dpi=400)
        print(filename + '파일 저장됨')

    # end def makeBarChart(self)
# end class Visualization

filename = '문재인대통령신년사.txt'
ko_con_text = open(filename, encoding='utf-8').read()
print(type(ko_con_text))
print('-'*30)

from PyKomoran import Komoran
komo = Komoran('STABLE')
# komo.set_user_dic('사용자정의파일.txt')

tokens_ko = komo.nouns(ko_con_text)
print(tokens_ko)
print('-'*30)

stop_word_file = 'stopword.txt'
stop_file = open(stop_word_file, 'rt', encoding='utf-8')
stop_words = [word.strip() for word in stop_file.readlines()]
print(stop_words)
print('-'*30)

print(len(tokens_ko))
tokens_ko = [each_word for each_word in tokens_ko if each_word not in stop_words]
print(len(tokens_ko))

import nltk
ko = nltk.Text(tokens=tokens_ko)
data = ko.vocab().most_common(500)
print(len(data))
print(data)
print('-'*30)

wordlist = list()

for word, count in data :
    if count >= 1 and len(word) >= 2 :
        wordlist.append((word, count))

print(wordlist)
print('-'*30)

visual = Visualization(wordlist)
visual.makeWordCloud()
visual.makeBarChart()
print('finished')