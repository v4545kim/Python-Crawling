import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
##########################################################
plt.rc('font', family='AppleGothic')
plt.rcParams['figure.figsize'] = [10, 5]
cnt, PNG, UNDERBAR = 0, '.png', '_'
CHART_NAME = 'brokenLineExam'
filename = './../data/주요발생국가주간동향(4월2째주).csv'
##########################################################
data = pd.read_csv(filename, index_col='국가')
print(data.columns)
print('-'*30)

print(data)
print('-'*30)

chartdata = data['4월06일']
print(type(chartdata))
print(chartdata)
print('-'*30)

plt.plot(chartdata, color='blue', linestyle='solid', marker='o')

YTICKS_INTERVAL = 50000
maxlim = (int(chartdata.max()/YTICKS_INTERVAL) + 1) * YTICKS_INTERVAL
print(maxlim)

values = np.arange(0, maxlim + 1, YTICKS_INTERVAL)
print(values)

plt.yticks(values, ['%s' % format(val, ',') for val in values])
plt.grid(True)
plt.xlabel('국가명')
plt.ylabel('발생 건수')
plt.title('4월06일 코로나 발생 건수')

cnt += 1
savefile = CHART_NAME + UNDERBAR + str(cnt).zfill(2) + PNG
plt.savefig(savefile, dpi=400)
print(savefile + '파일 저장됨')

COUNTRY = ['스페인', '프랑스', '독일', '중국', '영국', '이란']
WHEN = ['4월06일', '4월07일', '4월08일', '4월09일', '4월10일']
chartdata = data.loc[COUNTRY, WHEN]

chartdata = chartdata.T
print(chartdata)
print('-'*30)

chartdata.plot(title='Some Title', marker='o', rot=0, legend=True, figsize=(10, 6))

plt.grid(True)
plt.xlabel('일자')
plt.ylabel('국가명')
plt.title('일자병 국가명 꺾은 선')

cnt += 1
savefile = CHART_NAME + UNDERBAR + str(cnt).zfill(2) + PNG
plt.savefig(savefile, dpi=400)
print(savefile + '파일 저장됨')


tipsfile = './../data/tips.csv'
myframe = pd.read_csv(tipsfile)
print(type(myframe))
print(myframe.columns)

data_bill = myframe.loc[:, ['total_bill']]
data_tip = myframe.loc[:, ['tip']]

fig, ax1 = plt.subplots()
ax1.set_title('결제 금액과 tip(이중축)')

xrange = range(len(myframe))
color = 'tab:red'
ax1.set_ylabel('결제 금액', color=color)
ax1.plot(xrange, data_bill, color=color)
ax1.tick_params(axis='y', labelcolor=color)

ax2 = ax1.twinx()
color = 'tab:blue'
ax2.set_ylabel('팁(tip)', color=color)
ax2.plot(xrange, data_tip, color=color)
ax2.tick_params(axis='y', labelcolor=color)

fig.tight_layout()

cnt += 1
savefile = CHART_NAME + UNDERBAR + str(cnt).zfill(2) + PNG
plt.savefig(savefile, dpi=400)
print(savefile + '파일 저장됨')

##########################################################
print('finished')