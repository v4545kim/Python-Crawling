import pandas as pd
data = pd.DataFrame({'번호':['1', '2'],
                     '이름':['김','최'],
                     '점수':['100','200']})
print(data)
data.to_csv('aaaa.csv')