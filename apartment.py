import requests
from bs4 import BeautifulSoup
import openpyxl

wb = openpyxl.Workbook()
sheet = wb.active

sheet.append(['아파트 이름', '매매매물수', '전세매물수', '월세매물수'])

res = requests.get('https://m.land.naver.com/complex/info/134062?ptpNo=1', headers = {'User-Agent': 'Mozilla/5.0'})

soup = BeautifulSoup(res.content, 'html.parser')

box = soup.select_one('div.detail_summary_area')

apart_name = box.select_one('strong.detail_complex_title')
price_num = box.select('li.price_item')
sell_num = price_num[0].select_one('em.txt_price').text
rent_num = price_num[1].select_one('em.txt_price').text
rent_mon_num = price_num[2].select_one('em.txt_price').text

sheet.append([apart_name.text, sell_num, rent_num, rent_mon_num])
print(apart_name.text)
print(sell_num)
print(rent_num)
print(rent_mon_num)
wb.save('apartment.xlsx')
