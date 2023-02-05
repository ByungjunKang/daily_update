from bs4 import BeautifulSoup
import requests

url = 'https://finance.naver.com/item/sise.naver?code=068760'
html = requests.get(url, headers = {'User-agent' : 'Mozilla/5.0'}).text
bs = BeautifulSoup(html, 'lxml')    #파싱 방식을 속도가 가장 빠른 lxml로
pgrr = bs.find('td', class_='pgRR') #사이트 검사 기능으로 원하는 태그 찾은 후 검색
print(pgrr)
