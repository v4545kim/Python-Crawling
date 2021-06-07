from itertools import count
from ChickenUtil import ChickenStore
##########################################################
brandName = 'goobne'
base_url = 'https://www.goobne.co.kr/store/search_store.jsp'
##########################################################
def getData():
    savedData = []  # 엑셀로 저장될 리스트
    chknStore = ChickenStore(brandName, base_url)

    for page_idx in count():
        print('%s번째 페이지가 호출됨' % str(page_idx + 1))

        bEndPage = False # 마지막 페이지이면 True
        cmdJavaScript = "javascript:store.getList('%s')" % str(page_idx + 1)
        soup = chknStore.getWebDriver(cmdJavaScript)

        store_list = soup.find('tbody', attrs={'id':'store_list'})
        mytrlists = store_list.findAll('tr')
        # print(len(mytrlists))

        for onestore in mytrlists:
            mytdlists = onestore.findAll('td')
            if len(mytdlists) > 1 :
                store = onestore.select_one('td:nth-of-type(1)').get_text(strip=True)

                phone = onestore.select_one('td:nth-of-type(2)').a.string

                address = onestore.select_one('td:nth-of-type(3)').a.string

                imsi = str(address).split(' ')
                sido = imsi[0]
                gungu = imsi[1]
                savedData.append([brandName, store, sido, gungu, address, phone])
            else : # 마지막 페이지이면
                bEndPage = True
                break

        # if page_idx == 2:
        #     break

        if bEndPage == True :
            break


    #print(savedData)
    chknStore.save2Csv(savedData)

##########################################################
print(brandName + '매장 크롤링 시작')
getData()
print(brandName + '매장 크롤링 끝')