from pandas_datareader import data as pdr
import yfinance as yf
yf.pdr_override()
import matplotlib.pyplot as plt

dow = pdr.get_data_yahoo('^DJI', '2000-01-04')  #Dow
ndq = pdr.get_data_yahoo('^NDX', '2000-01-04')  #NASDAQ
kospi = pdr.get_data_yahoo('^KS11', '2000-01-04')

#DOW, KOSPI 지수화 비교
d = (dow.Close / dow.Close.loc['2000-01-04']) * 100
k = (kospi.Close / kospi.Close.loc['2000-01-04']) * 100
n = (ndq.Close / ndq.Close.loc['2000-01-04']) * 100

plt.figure(figsize=(9,5))
plt.plot(d.index, d, 'r--', label='Dow Jones Industrial Average')
plt.plot(n.index, n, 'g', label='NASDAQ')
plt.plot(k.index, k, 'b', label='KOSPI')
plt.grid(True)
plt.legend(loc='best')
plt.show()

#산점도 분석
import pandas as pd
df = pd.DataFrame({'DOW': dow['Close'], 'KOSPI': kospi['Close']})
df = df.fillna(method='bfill')
df = df.fillna(method='ffill')

plt.figure(figsize=(7,7))
plt.scatter(df['DOW'], df['KOSPI'], marker='.')
plt.xlabel('Dow Jones Industrial Average')
plt.ylabel('KOSPI')
plt.show()

#선형회귀 모델
from scipy import stats
regr = stats.linregress(df['DOW'], df['KOSPI'])

#결정계수(R-squared)
r_value = df['DOW'].corr(df['KOSPI'])
r_squared = r_value ** 2
