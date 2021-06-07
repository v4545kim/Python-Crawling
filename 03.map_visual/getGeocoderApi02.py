import  folium
import pandas as pd
import requests
url_header = 'https://dapi.kakao.com/v2/local/search/address.json?query='

api_key = '1bd1923d9a6232e5829a4976b85dbe3a'
header = {'Authorization': 'KakaoAK ' + api_key}

def getGeocoder(address) :
    result = ''
    url = url_header + address

    r = requests.get(url, headers=header)

    if r.status_code == 200 :
        try :
            result_address = r.json()["documents"][0]["address"]
            result = result_address['y'], result_address['x']
        except Exception as err :
            return  None
    else :
        result = 'Error[' + str(r.status_code) + ']'
    return result
#end def getGeocoder(address):

def makeMap(brand, store, geoInfo) :
    shopinfo = store + '(' + brand_dict[brand] + ')'
    mycolor = brand_color[brand]
    latitude, longitude = float(geoInfo[0]), float(geoInfo[1])

    # 마커 그리기
    folium.Marker([latitude, longitude], popup=shopinfo,
                  icon=folium.Icon(color=mycolor, icon='info-sign')).add_to(mapObject)
# end makeMap(brand, store, geoInfo)

brand_dict = {'cheogajip':'처가집', 'goobne':'굽네', 'pelicana':'페리카나', 'nene':'네네'}
brand_color = {'cheogajip':'red', 'goobne':'green', 'pelicana':'yellow', 'nene':'blue'}

# 지도의 기준점
mylatitude = 37.56
mylongitude = 126.92
mapObject = folium.Map(location=[mylatitude, mylongitude], zoom_start=13)

csv_file = './../02.crawling/allStoreModified.csv'
myframe = pd.read_csv(csv_file, index_col=0, encoding='utf-8')
# print(myframe.info())

where = '서대문구'
brandName = 'cheogajip'
condition1 = myframe['gungu'] == where
condition2 = myframe['brand'] == brandName
mapData01 = myframe.loc[condition1 & condition2]
# print(mapData01)

brandName = 'nene'
condition1 = myframe['gungu'] == where
condition2 = myframe['brand'] == brandName
mapData02 = myframe.loc[condition1 & condition2]
# print(mapData02)


mylist = []
mylist.append(mapData01)
mylist.append(mapData02)

mapData = pd.concat(mylist, axis=0)
# print(mapData)

ok, notok = 0, 0
for idx in range(len(mapData.index)) :
    brand = mapData.iloc[idx]['brand']
    store = mapData.iloc[idx]['store']
    address = mapData.iloc[idx]['address']
    geoInfo = getGeocoder(address)

    if geoInfo == None :
        print('낫오케이 : ' + address)
        notok += 1
    else :
        print('오케이 : ' + address)
        ok += 1
        makeMap(brand, store, geoInfo)
    print('-'*30)

total = ok + notok
print('ok : ', ok)
print('notok : ', notok)
print('total : ', total)

filename = '/Users/gimsunseob/desktop/파이썬/mapresult.html'
mapObject.save(filename)
print('파일 저장 완료')

