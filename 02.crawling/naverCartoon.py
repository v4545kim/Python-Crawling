weekday_dict = {'mon':'월요일', 'tue':'화요일', 'wed':'수요일',
                'thu':'목요일', 'fri':'금요일', 'sat':'토요일',
                'sun':'일요일'}
# 파이썬에서 주석은 #으로 시작하고, 단축키는 cmd(ctrl) + / 입니다.
# print(weekday_dict)
# print('-'*30)
#
# print(weekday_dict.keys())
# print('-'*30)
#
# print(weekday_dict.values())
# print('-'*30)

import os
myfolder = '/Users/gimsunseob/Desktop/파이썬/imsi/'

try :
    if not os.path.exists(myfolder):
        os.mkdir(myfolder)

    for mydir in weekday_dict.values():
        mypath = myfolder + mydir
        if os.path.exists(mypath):
            pass
        else :
            os.mkdir(mypath)
except FileExistsError as err:
    pass

# str = 'id=hong&password=1234'
# result = str.split('&')
# print(result)
# print(result[0])
#
# id = result[0].split('=')[1]
# password = result[1].split('=')[1]
#
# print(id)
# print(password)
#
# str2 = 'abc?:def'
# str2 = str2.replace('?', '').replace(':', '')
# print(str2)


from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# 사이트의 이미지 파일을 해당 요일 폴더에 저장합니다.
def saveFile(mysrc, mywekkday, mytitle):
    image_file = urlopen(mysrc, context=context)
    filename = myfolder + mywekkday + '/' + mytitle + '.jpg'
    # print(filename)

    myfile = open(filename, mode='wb')
    # 바이너리 형태로  변경하여 기록합니다.
    myfile.write(image_file.read())

context = ssl._create_unverified_context()
myparser = 'html.parser'
myurl = 'https://comic.naver.com/webtoon/weekday.nhn'
response = urlopen(myurl, context=context)
soup = BeautifulSoup(response, myparser)
print(type(soup)) #<class 'bs4.BeautifulSoup'>

mytarget = soup.find_all('div', attrs={'class':'thumb'})

print('총 개수 : %d' % len(mytarget))

mylist = [] # 목록을 저장할 리스트
for abcd in mytarget :
    myhref = abcd.find('a').attrs['href']
    myhref = myhref.replace('/webtoon/list.nhn?', '')
    result = myhref.split('&')
    mytitleid = result[0].split('=')[1]
    myweekday = result[1].split('=')[1]
    myweekday = weekday_dict[myweekday]
    # print(mytitleid + '/' + myweekday)

    imgtag = abcd.find('img')
    mysrc = imgtag.attrs['src']
    # print(mysrc)

    mytitle = imgtag.attrs['title'].strip()
    mytitle = mytitle.replace('?', '').replace(':', '')
    # print(mytitle)

    mylist.append((mytitleid, myweekday, mytitle, mysrc))

    saveFile(mysrc, myweekday, mytitle)

print('리스트 내용 보기')
print(mylist)







# saveFile('a.jpg', '월요일', '여신강림')

# mylist.append((1, '김', 100))
# mylist.append((2, '최', 200))
# print(mylist)

# 판다스에 들어있는 DataFrame을 사용합니다.
from pandas import DataFrame

myframe = DataFrame(mylist, columns=['타이틀 번호', '요일', '제목', '링크'])
filename = 'cartoon.csv'
myframe.to_csv(filename, encoding='utf-8', index=False)



print('finished')








