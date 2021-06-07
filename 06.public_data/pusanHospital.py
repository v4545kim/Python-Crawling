import datetime, json, math
import urllib.request

def getRequestUrl(url):
    req = urllib.request.Request(url)
    try:
        response = urllib.request.urlopen(req)
        if response.getcode() == 200:
            # print(('[%s] success' % (datetime.datetime.now())))
            return response.read().decode('utf-8')
    except Exception as e:
        print(('[%s] failure' % (datetime.datetime.now())))
        print(e)
        return None
# end def getRequestUrl(url):

def getHospitalData(pageNo, numOfRows):
    end_point = 'http://apis.data.go.kr/6260000/MedicInstitService/MedicalInstitInfo'

    access_key = 'Wu5PoGsZoaO%2BB3xtH7CTNDe%2FEJfK1XPwC3vDUnxc0yyWeJhcoBqgPsXSTb5YDSR19g65BZY6hN4hKBrcFxvMEw%3D%3D'

    parameters = '?resultType=json'
    parameters += '&serviceKey=' + access_key
    parameters += '&pageNo=' + str(pageNo)
    parameters += '&numOfRows=' + str(numOfRows)

    url = end_point + parameters
    # print('유알엘')
    print(url)

    result = getRequestUrl(url)
    if (result == None):
        return  None
    else:
        return json.loads(result)
# end def getHospitalData(pageNo, numOfRows):

jsonResult = []

pageNo = 1 # 페이지 번호
numOfRows = 100 # 1번에 조회할 최대 행수
nPage = 0

while True:
    print('pageNo : %d, nPage : %d' % (pageNo, nPage))
    jsonData = getHospitalData(pageNo, numOfRows)
    # print(jsonData)
    # print('-'*30)

    if(jsonData['MedicalInstitInfo']['header']['code'] == '00'):
        totalCount = jsonData['MedicalInstitInfo']['totalCount']
        # print('데이터 총 갯수 : ' + str(totalCount))

        if totalCount == 0:
            break

        for item in jsonData['MedicalInstitInfo']['item']:
            jsonResult.append(item)

        nPage = math.ceil(totalCount/numOfRows)
        if(pageNo == nPage):
            break # 마지막 페이지입니다.

        pageNo += 1
    else:
        break

    savedFilename = '부산시 의료 기관, 약국 운영 시간 정보.json'
    with open(savedFilename, 'w', encoding='utf-8') as outfile:
        retJson = json.dumps(jsonResult, indent=4, sort_keys=True, ensure_ascii=False)
        outfile.write(retJson)
    print(savedFilename + '파일 저장됨')
# print(len(jsonResult))

print('finished')