import pandas as pd

csv_file = './../02.crawling/allStoreModified.csv'
myframe = pd.read_csv(csv_file, index_col=0, encoding='utf-8')
print(myframe.info())
print('-'*30)

print(myframe['brand'].unique())
print('-'*30)

mygrouping = myframe.groupby(['brand'])['brand']
print(type(mygrouping))
print('-'*30)

chartdata = mygrouping.count()
print(type(chartdata))
print(chartdata)
print('-'*30)

mycolor = ['r', 'g', 'b', 'm']

print(chartdata.index)
print('-'*30)

brand_dict = {'cheogajip':'처가집', 'goobne':'굽네', 'pelicana':'페리카나', 'nene':'네네'}
newindex = [brand_dict[idx] for idx in chartdata.index]
chartdata.index = newindex

print(chartdata.index)
print('-'*30)

import matplotlib.pyplot as plt

plt.rcParams['font.family'] = 'AppleGothic' # 맥에는 Malgun Gothic(맑은고딕)이 없어서 기본 글꼴인 AppleGothic을 사용한다.

plt.figure()
chartdata.plot(kind='pie', legend=False, autopct='%1.2f%%', colors=mycolor)
filename = 'makeChickenGraph01.png'
plt.savefig(filename, dpi=400)
print(filename + '파일이 저장되었습니다.')


plt.figure()
chartdata.plot(kind='barh', legend=False, title='브랜드 별 총 매장 갯수', rot=30, color=mycolor)
filename = 'makeChickenGraph02.png'
plt.savefig(filename, dpi=400)
print(filename + '파일이 저장되었습니다.')
# plt.show()
