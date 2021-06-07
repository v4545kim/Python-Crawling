import matplotlib.pyplot as plt
from wordcloud import WordCloud

filename = 'steve.txt'
myfile = open(filename, 'rt', encoding='utf-8')
text = myfile.read()
print(type(text))
print('-'*30)

wordcloud = WordCloud()
wordcloud = wordcloud.generate(text)
print(type(wordcloud))
print('-'*30)

bindo = wordcloud.words_
print(type(bindo))
print(bindo)
print('-'*30)

sortedData = sorted(bindo.items(), key=lambda x : x[1], reverse=True)
print(len(sortedData))
print(type(sortedData))
print(sortedData)
print('-'*30)

chartData = sortedData[0:10]
print(chartData)
print('-'*30)

xtick = []
chart = []
for item in chartData:
    xtick.append(item[0])
    chart.append(item[1])

plt.rc('font', family='AppleGothic')

mycolor = ['r', 'g', 'b', 'y', 'm', 'c', '#FFF0F0', '#CCFFBB', '#05CCFF', '#11CCFF']
plt.bar(xtick, chart, color=mycolor)
plt.title('상위 빈도 Top 10')
filename = 'wordCloudEx01_01.png'
plt.savefig(filename, dpi=400, bbox_inches='tight')
print(filename + '파일이 저장되었습니다.')


plt.figure(figsize=(12,12))
plt.imshow(wordcloud)
plt.axis('off')

filename = 'wordCloudEx01_02.png'
plt.savefig(filename, dpi=400, bbox_inches='tight')
print(filename + '파일이 저장되었습니다.')
