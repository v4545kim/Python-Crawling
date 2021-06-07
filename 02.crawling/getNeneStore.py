import re # 정규 표현식 모듈

from ChickenUtil import ChickenStore
##########################################################
brandName = 'nene'
base_url = 'https://nenechicken.com/17_new/sub_shop01.asp'
##########################################################
def getData():
    savedData = []  # 엑셀로 저장될 리스트

    for page_idx in range(1, 46+1):
        url = base_url + '?page=%d' % (page_idx)
        chknStore = ChickenStore(brandName, url)
        soup = chknStore.getSoup()
        # print(type(soup))

        tablelists = soup.findAll('table', attrs={'class':'shopTable'})
        # print(len(tablelists))
        for onetable in tablelists :
            store = onetable.select_one('.shopName').string
            # print(store)

            temp = onetable.select_one('.shopAdd').string
            if temp == None:
                continue

            # print('temp')
            # print(temp)

            imsi = temp.split()
            sido = imsi[0]
            gungu = imsi[1]
            # print(sido + '/' + gungu)

            # 주소 접미사
            im_address = onetable.select_one('.shopMap')
            im_address = im_address.a['href']

            # 정규 표현식으로 숫자가 처음으로 나오는 위치부터 문자열 추출
            regex = '\d\S*' # 숫자로 시작하는 ....
            pattern = re.compile(regex)
            mymatch = pattern.search(im_address)
            addr_suffix = mymatch.group().replace("');", '')
            # print(addr_suffix)
            # print(im_address)

            address = temp + ' ' + addr_suffix

            phone = onetable.select_one('.tooltiptext').string

            mydata = [brandName, store, sido, gungu, address, phone]
            savedData.append(mydata)

    # print(savedData)

    chknStore.save2Csv(savedData)

##########################################################
print(brandName + '매장 크롤링 시작')
getData()
print(brandName + '매장 크롤링 끝')