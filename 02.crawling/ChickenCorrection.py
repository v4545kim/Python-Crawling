import numpy as np
import pandas as pd

pd.options.display.max_columns = 1000
pd.options.display.max_rows = 1000

class ChickenCorrection():
    myencoding = 'utf-8'

    def __init__(self,workfile):
        self.workfile = workfile
        self.myframe = pd.read_csv(self.workfile, encoding=self.myencoding, index_col=0)

        # print(self.myframe.head())
        # print(self.myframe.info())

        self.correctioonSido()
        self.correctioonGungu()
        self.showMergeResult()
        self.correctioonAddress()

        self.myframe.to_csv('allStoreModified.csv', encoding=self.myencoding)
        print('파일 저장 완료')

    def correctioonSido(self):
        self.myframe = self.myframe[self.myframe['store'] != 'CNTTEST']
        self.myframe = self.myframe[self.myframe['sido'] != '테스트']

        # print('before sido')
        # print(np.sort(self.myframe['sido'].unique()))
        # print('-'*40)

        sidofile = open('sido_correction.txt', 'r', encoding=self.myencoding)
        linelists = sidofile.readlines()
        # print(type(linelists))
        # print(linelists)

        sido_dict = {} # dict()
        for oneline in linelists:
            mydata = oneline.replace('\n', '').split(':')
            # print(mydata)
            sido_dict[mydata[0]] = mydata[1]

        # print(sido_dict)

        self.myframe.sido = \
            self.myframe.sido.apply(lambda data : sido_dict.get(data, data))


        # print('after sido')
        # print(np.sort(self.myframe['sido'].unique()))
        # print('-' * 40)

    #end def correctionSido(self)


    def correctioonGungu(self):
        # print('before gungu')
        # print(self.myframe['gungu'].unique())
        # print('-'*40)

        gungufile = open('gungu_correction.txt', 'r', encoding=self.myencoding)
        linelists = gungufile.readlines()

        gungu_dict = {}
        for oneline in linelists:
            mydata = oneline.replace('\n', '').split(':')
            gungu_dict[mydata[0]] = mydata[1]

        self.myframe.gungu = self.myframe.gungu.apply(lambda data : gungu_dict.get(data, data))

        # print('after gungu')
        # print(self.myframe['gungu'].unique())
        # print('-' * 40)

    def showMergeResult(self):
        district = pd.read_csv('district.csv', encoding=self.myencoding)
        # print(district.info())

        mergedata = pd.merge(self.myframe, district, on=['sido', 'gungu'],
                             how='outer', suffixes=['', '_'], indicator=True)

        # print(mergedata.head(10))

        result = mergedata.query('_merge == "left_only"')
        # print('좌측에만 있는 데이터')
        # print(result[['sido', 'gungu', 'address']])


    def correctioonAddress(self):
        try :
            for idx in range(len(self.myframe)):
                imsiseries = self.myframe.iloc[idx]
                # print(imsiseries)
                addrSplit = imsiseries['address'].split(' ')[2:]
                # print(addrSplit)
                imsiAddress = [imsiseries['sido'], imsiseries['gungu']]
                imsiAddress = imsiAddress + addrSplit
                # print(imsiAddress)

                self.myframe.iloc[idx]['address'] = ' '.join(imsiAddress)

                print('-'*30)
        except TypeError as err:
            pass


filename = 'allstore.csv'
chknStore = ChickenCorrection(filename)
print('finished')