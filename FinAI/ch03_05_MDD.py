from pandas_datareader import data as pdr
import yfinance as yf
yf.pdr_override()
import matplotlib.pyplot as plt

kospi = pdr.get_data_yahoo('^KS11', '2004-01-04')

window = 252    #1년 개장일
peak = kospi['Adj Close'].rolling(window, min_periods=1).max()   #1년간 peak값
drawdown = kospi['Adj Close']/peak - 1.0
max_dd = drawdown.rolling(window, min_periods=1).min()  #1년간 max drawback

plt.figure(figsize=(9,7))
plt.subplot(211)    #2행1열 중 1행에 그림
kospi['Close'].plot(label='KOSPI', title='KOSPI MDD', grid=True, legend=True)
plt.subplot(212)    #2행1열 중 2행에 그림
drawdown.plot(c='blue', label='KOSPI DD', grid=True, legend=True)
max_dd.plot(c='red', label='KOSPI MDD', grid=True, legend=True)
plt.show()

