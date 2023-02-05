from pandas_datareader import data as pdr
import yfinance as yf
yf.pdr_override()

sec = pdr.get_data_yahoo('005930.KS', "2020-03-01", "2022-12-30")
msft = pdr.get_data_yahoo('MSFT', "2020-03-01", "2022-12-30")

sec_dpc = (sec['Close']-sec['Close'].shift(1)) / sec['Close'].shift(1) * 100
sec_dpc.iloc[0] = 0
msft_dpc = (msft['Close']-msft['Close'].shift(1)) / msft['Close'].shift(1) * 100
msft_dpc.iloc[0] = 0

import matplotlib.pyplot as plt
#종가 그리기
#plt.plot(sec.index, sec.Close, 'b', label='Samsung Electronics')
#plt.plot(msft.index, msft.Close, 'r--', label='Microsoft')
#plt.legend(loc='best')
#plt.show()

#일간 변동률 그리기
#plt.hist(sec_dpc, bins=18)
#plt.grid(True)
#plt.show()

#일간 변동률 누적곱 그리기
sec_dpc_cp = ((100+sec_dpc)/100).cumprod()*100-100
msft_dpc_cp = ((100+msft_dpc)/100).cumprod()*100-100
plt.plot(sec.index, sec_dpc_cp, 'b', label='Samsung Electronics')
plt.plot(msft.index, msft_dpc_cp, 'r--', label='Microsoft')
plt.ylabel('Change %')
plt.grid(True)
plt.legend(loc='best')
plt.show()
