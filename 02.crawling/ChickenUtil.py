import ssl, datetime
import time
import urllib.request
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver

class ChickenStore():
    def getWebDriver(self, cmdJavaScript):
        # cmdJavaScript : 문자열로 구성된 자바 스크립트 커맨드
        print(cmdJavaScript)
        self.driver.execute_script(cmdJavaScript)
        wait = 5
        time.sleep(wait)
        mypage = self.driver.page_source

        return BeautifulSoup(mypage, 'html.parser')

    def save2Csv(self,result):
        mycolumn = ['brand', 'store', 'sido', 'gungu', 'address', 'phone']
        data = pd.DataFrame(result, columns=mycolumn)
        data.to_csv(self.brandName + '.csv', encoding='utf-8', index=True)
        print(self.brandName + '파일이 생성됨')

    def getSoup(self):
        if self.soup == None:
            return None
        else:
            return BeautifulSoup(self.soup, 'html.parser')

    def get_request_url(self):
        request = urllib.request.Request(self.url)
        try:
            context = ssl._create_unverified_context()
            response = urllib.request.urlopen(request, context=context)
            if response.getcode() == 200:
                # print('[%s] url request success' % datetime.datetime.now())

                if self.brandName != 'pelicana':
                    return response.read().decode('utf-8')
                else:
                    return response

        except Exception as err:
            print(err)
            now = datetime.datetime.now()
            msg = '[%s] error for url %s' % (now, self.url)
            print(msg)
            return None

    def __init__(self, brandName, url):
        self.brandName = brandName
        self.url = url

        if self.brandName != 'goobne':
            self.soup = self.get_request_url()
            self.driver = None
        else : # 굽네 매장
            self.soup = None
            filepath = '/Users/gimsunseob/desktop/파이썬/chromedriver'
            self.driver = webdriver.Chrome(filepath)
            self.driver.get(self.url)