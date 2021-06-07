import pandas as pd
import matplotlib.pyplot as plt
##########################################################
plt.rc('font', family='AppleGothic')
cnt, PNG, UNDERBAR = 0, '.png', '_'
CHART_NAME = 'scatterPlotExam'
filename = './../data/mpg.csv'
##########################################################
print('스타일 목록')
print(plt.style.available)
print('-'*30)

plt.style.use('ggplot')

mpg = pd.read_csv(filename, encoding='utf-8')
print(mpg.columns)
print('-'*30)

xdata = mpg.loc[:, ['displ']]  # 엔진 크기
ydata = mpg.loc[:, ['hwy']]  # 주행 마일수

plt.figure()
plt.plot(xdata, ydata, linestyle='None', marker='o')
plt.xlabel('엔진 크기')
plt.ylabel('주행 마일수')
plt.title('산점도 그래프')
plt.grid(True)

cnt += 1
savefile = CHART_NAME + UNDERBAR + str(cnt).zfill(2) + PNG
plt.savefig(savefile, dpi=400)
print(savefile + '파일 저장됨')

labels = mpg['drv'].unique()
print(labels)  # ['f' '4' 'r']

mycolor = ['r', 'g', 'b']
plt.figure()
idx = 0
labels_dict = {'f':'전륜 구동', '4':'사륜 구동', 'r':'후륜 구동'}

for finditem in labels:
    xdata = mpg.loc[mpg['drv'] == finditem, 'displ']
    ydata = mpg.loc[mpg['drv'] == finditem, 'hwy']
    plt.plot(xdata, ydata, linestyle='None', marker='o', label=labels_dict[finditem], color=mycolor[idx])
    idx += 1

plt.legend()
plt.xlabel('엔진 크기')
plt.ylabel('주행 마일수')
plt.title('산점도 그래프')
plt.grid(True)

cnt += 1
savefile = CHART_NAME + UNDERBAR + str(cnt).zfill(2) + PNG
plt.savefig(savefile, dpi=400)
print(savefile + '파일 저장됨')


# Create Fig and gridspec
fig = plt.figure(figsize=(16, 10), dpi= 80)
grid = plt.GridSpec(4, 4, hspace=0.5, wspace=0.2)

# 축을 정의합니다.
ax_main = fig.add_subplot(grid[:-1, :-1])
ax_right = fig.add_subplot(grid[:-1, -1], xticklabels=[], yticklabels=[])
ax_bottom = fig.add_subplot(grid[-1, 0:-1], xticklabels=[], yticklabels=[])

# 메인 그래프에 산점도를 그립니다.
ax_main.scatter('displ', 'hwy', s=mpg.cty*4, c=mpg.manufacturer.astype('category').cat.codes, alpha=.9, data=mpg, cmap="tab10", edgecolors='gray', linewidths=.5)

# 하단의 histogram
ax_bottom.hist(mpg.displ, 40, histtype='stepfilled', orientation='vertical', color='lightpink')
ax_bottom.invert_yaxis()

# 오른쪽 histogram
ax_right.hist(mpg.hwy, 40, histtype='stepfilled', orientation='horizontal', color='lightblue')

# Decorations
ax_main.set(title='산점도(엔진의 크기 vs 주행 마일수)', xlabel='엔진의 크기', ylabel='주행 마일수')
ax_main.title.set_fontsize(20)
for item in ([ax_main.xaxis.label, ax_main.yaxis.label] + ax_main.get_xticklabels() + ax_main.get_yticklabels()):
    item.set_fontsize(14)

xlabels = ax_main.get_xticks().tolist()

cnt += 1
savefile = CHART_NAME + UNDERBAR + str(cnt).zfill(2) + PNG
plt.savefig(savefile, dpi=400)
print(savefile + ' 파일이 저장되었습니다.')

# carat(무게), cut(품질), color(색상), clarity, depth,
# table, price(가격)

# 샘플링
# price와 depth를 이용한 산점도 그래프
# table을 이용하여 원의 크기를 다르게 만들기
diamond_file = './../data/diamonds.csv'

diamonds = pd.read_csv(diamond_file)
FRACTION = 0.005
diamonds = diamonds.sample(frac=FRACTION)

xdata = diamonds['price']
ydata = diamonds['depth']
table = diamonds['table']

mycolor = ['r', 'g', 'b', 'y', 'm']
cut_list = diamonds['cut'].unique()
print(cut_list)
print('-'*30)

cut_dict = { cut_list[idx]:mycolor[idx] for idx in range(len(cut_list))}
print(cut_dict)
print('-'*30)

def record_cut(cut):
    return cut_dict[cut]

diamonds['newcut'] = diamonds['cut'].apply(record_cut)
newcut = diamonds['newcut']

def record_table(table):
    if table >= 60:
        return 100
    elif table >= 58:
        return 30
    elif table >- 54:
        return 5
    else:
        return 1

diamonds['newtable'] = diamonds['table' ].apply(record_table)
newtable =  diamonds['newtable']

scatter_plot = plt.figure()
ax1 = scatter_plot.add_subplot(1, 1, 1)
ax1.scatter(x=xdata, y=ydata, s=newtable, c=newcut)

cnt += 1
savefile = CHART_NAME + UNDERBAR + str(cnt).zfill(2) + PNG
plt.savefig(savefile, dpi=400)
print(savefile + ' 파일이 저장되었습니다.')