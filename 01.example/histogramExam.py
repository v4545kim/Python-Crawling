import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
##########################################################
plt.rc('font', family='AppleGothic')
cnt, PNG, UNDERBAR = 0, '.png', '_'
CHART_NAME = 'histogramExam'
filename = './../data/tips.csv'
##########################################################
tips = pd.read_csv(filename, encoding='utf-8')
print(tips.columns)
print('-'*30)

x = tips['total_bill']
print(type(x))

num_bins = 30
fig, ax = plt.subplots()
n, bins, patches = ax.hist(x, num_bins, density=True)

ax.set_title('히스토그램')
ax.set_xlabel('Frequency')
ax.set_ylabel('total bill')

import numpy as np

mu = x.mean()  # 평균
print('mu :', mu)

sigma = x.std()  # 표준 편차
print('sigma :', sigma)

y = ((1 / (np.sqrt(2 * np.pi) * sigma)) *
     np.exp(-0.5 * (1 / sigma * (bins - mu))**2))
ax.plot(bins, y, '--')

# Tweak spacing to prevent clipping of ylabel
fig.tight_layout()

cnt += 1
savefile = CHART_NAME + UNDERBAR + str(cnt).zfill(2) + PNG
plt.savefig(savefile, dpi=400)
print(savefile + '파일 저장됨')

humanfile = './../data/human_height.csv'
human = pd.read_csv(humanfile, encoding='utf-8')

fig, axes = plt.subplots(nrows=1, ncols=2)
giant = human['giant']
dwarf = human['dwarf']

axes[0].hist(giant, range=(210, 290), bins=20, alpha=0.6)
axes[1].hist(dwarf, range=(100, 180), bins=20, alpha=0.6)

axes[0].set_title('거인국의 키')
axes[1].set_title('소인국의 키')

cnt += 1
savefile = CHART_NAME + UNDERBAR + str(cnt).zfill(2) + PNG
plt.savefig(savefile, dpi=400)
print(savefile + '파일 저장됨')

fig, axes = plt.subplots()
axes.hist(giant, bins=20, alpha=0.6)
axes.hist(dwarf, bins=20, alpha=0.6)

cnt += 1
savefile = CHART_NAME + UNDERBAR + str(cnt).zfill(2) + PNG
plt.savefig(savefile, dpi=400)
print(savefile + '파일 저장됨')

fig, axes = plt.subplots()
man = human['man']
woman = human['woman']
x = np.array([man, woman]).T

print(x.shape)  # shape는 형상
print(type(x.shape))

axes.hist(x, bins=num_bins, density=False, histtype='bar', stacked=True)
axes.set_title('누적 히스토그램')

cnt += 1
savefile = CHART_NAME + UNDERBAR + str(cnt).zfill(2) + PNG
plt.savefig(savefile, dpi=400)
print(savefile + '파일 저장됨')