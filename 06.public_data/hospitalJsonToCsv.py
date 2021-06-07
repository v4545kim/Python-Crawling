import json

jsonfile = '부산시 의료 기관, 약국 운영 시간 정보.json'

myfile = open(jsonfile, 'rt', encoding='utf-8')
myfile = myfile.read()

jsonData = json.loads(myfile)
print(type(jsonData))
print('-'*30)

totallist = []
mycolumns = [] # 컬럼 이름
idx = 0
for oneitem in jsonData:
    # print(type(oneitem))
    sublist = []
    for key in oneitem.keys():
        # print(key)
        if idx == 0:
            mycolumns.append(key)

        sublist.append(oneitem[key])
    idx += 1

    totallist.append(sublist)
    print('-'*30)

print(totallist)

from pandas import  DataFrame

myframe = DataFrame(totallist, columns=mycolumns)
filename = 'pusanHospitalExcel.csv'
myframe.to_csv(filename, encoding='utf-8', index=False)
print('finished')