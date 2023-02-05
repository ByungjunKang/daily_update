import requests
from bs4 import BeautifulSoup
import openpyxl
from datetime import datetime
import pandas as pd

wb = openpyxl.Workbook()
sheet = wb.active

sheet.append(['날짜', '아파트 이름', '매매매물수', '전세매물수', '월세매물수', '25평 최소가격'])

sites = ['https://m.land.naver.com/complex/info/119219?ptpNo=9',
         'https://m.land.naver.com/complex/info/134062?ptpNo=1',
         'https://m.land.naver.com/complex/info/112228?ptpNo=1',
         'https://m.land.naver.com/complex/info/113151?ptpNo=24',
         'https://m.land.naver.com/complex/info/128527?ptpNo=1',
         'https://m.land.naver.com/complex/info/1298?ptpNo=1',
         'https://m.land.naver.com/complex/info/1303?ptpNo=1',
         'https://m.land.naver.com/complex/info/1307?ptpNo=1',
         'https://m.land.naver.com/complex/info/121971?ptpNo=1',
         'https://m.land.naver.com/complex/info/113125?ptpNo=1']

sites_price = ['https://m.land.naver.com/complex/info/119219?tradTpCd=A1&ptpNo=1:10&bildNo=&articleListYN=Y',
               'https://m.land.naver.com/complex/info/134062?tradTpCd=A1&ptpNo=5:6&bildNo=&articleListYN=Y',
               'https://m.land.naver.com/complex/info/112228?tradTpCd=A1&ptpNo=2:16:3:17&bildNo=&articleListYN=Y',
               'https://m.land.naver.com/complex/info/113151?tradTpCd=A1&ptpNo=20:25:30&bildNo=&articleListYN=Y',
               'https://m.land.naver.com/complex/info/128527?tradTpCd=A1&ptpNo=6:4:5&bildNo=&articleListYN=Y',
               'https://m.land.naver.com/complex/info/1298?tradTpCd=A1&ptpNo=2&bildNo=&articleListYN=Y',
               'https://m.land.naver.com/complex/info/1303?tradTpCd=A1&ptpNo=2&bildNo=&articleListYN=Y',
               'https://m.land.naver.com/complex/info/1307?tradTpCd=A1&ptpNo=2&bildNo=&articleListYN=Y',
               'https://m.land.naver.com/complex/info/121971?tradTpCd=A1&ptpNo=1:3:2&bildNo=&articleListYN=Y',
               'https://m.land.naver.com/complex/info/113125?tradTpCd=A1&ptpNo=1:2:3&bildNo=&articleListYN=Y']

gaepo_name = ['개시', '개1', '개2', '개3', '개4', '개5', '개6', '개7', '개8', '개9']

gaepo_num = pd.Series(sites, index = gaepo_name, name = 'number')
gaepo_price_25 = pd.Series(sites_price, index = gaepo_name, name = 'price_25')
df = pd.DataFrame({gaepo_num.name: gaepo_num, gaepo_price_25.name: gaepo_price_25})

for i in df.index:
    res = requests.get(df['number'][i], headers = {'User-Agent': 'Mozilla/5.0'})
    soup = BeautifulSoup(res.content, 'html.parser')
    box = soup.select_one('div.detail_summary_area')

    apart_name = box.select_one('strong.detail_complex_title')
    price_num = box.select('li.price_item')
    sell_num = price_num[0].select_one('em.txt_price').text
    rent_num = price_num[1].select_one('em.txt_price').text
    rent_mon_num = price_num[2].select_one('em.txt_price').text

    res_p = requests.get(df['price_25'][i], headers = {'User-Agent': 'Mozilla/5.0'})
    soup_p = BeautifulSoup(res_p.content, 'html.parser')
    box_p = soup_p.select('strong.price')
    min_price_25 = 50;
    for pr in box_p:
        price_25_temp = int(pr.text.replace('억',''))
        if min_price_25 > price_25_temp:
            min_price_25 = price_25_temp

    sheet.append([datetime.now().date(), apart_name.text, sell_num, rent_num, rent_mon_num, min_price_25])
    print(datetime.now().date())
    print(apart_name.text)
    print(sell_num)
    print(rent_num)
    print(rent_mon_num)
    wb.save('apartment_gaepo.xlsx')
