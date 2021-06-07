import pandas as pd
from pandas import DataFrame

myencoding = 'utf-8'
chikenList = ['pelicana', 'nene', 'cheogajip', 'goobne']
# chikenList = ['pelicana']

newframe = DataFrame()

for onestore in chikenList:
    filename = onestore + '.csv'
    myframe = pd.read_csv(filename, index_col=0, encoding=myencoding)
    # print(myframe.head())
    # print('-'*30)
    newframe = pd.concat([newframe, myframe], axis=0, ignore_index=True)

print(newframe.info())

totalfile = 'allstore.csv'
newframe.to_csv(totalfile, encoding=myencoding)
print(totalfile + '파일이 저장됨')