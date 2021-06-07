from ChickenUtil import ChickenStore
from itertools import count
##########################################################
brandName = 'pelicana'
base_url = 'https://pelicana.co.kr/store/stroe_search.html'
##########################################################
def getData():
    savedData = []  # 엑셀로 저장될 리스트

    for page_idx in count():
        url = base_url + '?page=' + str(page_idx + 1)
        chknStore = ChickenStore(brandName, url)
        soup = chknStore.getSoup()
        # print(type(soup))

        if soup != None:
            mytable = soup.find('table', attrs={'class':'table mt20'})
        mytbody = mytable.find('tbody')

        shopExists = False # 목록이 없다고 가정

        for mytr in mytbody.findAll('tr'):
            shopExists = True
            imsiphone = mytr.select_one('td:nth-of-type(3)').string
            if imsiphone != None :
                phone = imsiphone.strip()
            else :
                phone =''
            # print(phone)

            mylist = list(mytr.strings)
            # print(mylist)
            # print('-'*30)

            store = mylist[1]
            # print(store)
            address = mylist[3]
            # print(address)

            if len(address) >= 2 :
                imsi = address.split()
                sido = imsi[0]
                gungu = imsi[1]
                # print(sido)
                # print(gungu)

                mydata = [brandName, store, sido, gungu, address, phone]
                savedData.append(mydata)

        if shopExists == False :
            chknStore.save2Csv(savedData)
            break

##########################################################
print(brandName + '매장 크롤링 시작')
getData()
print(brandName + '매장 크롤링 끝')