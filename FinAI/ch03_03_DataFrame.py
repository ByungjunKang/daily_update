import pandas as pd
#dictionary 형태로 직접 입력
#df = pd.DataFrame({'KOSPI':[1915, 1961, 2026, 2467, 2041],
#                   'KOSDAQ':[542, 682, 631, 798, 675]})

#Series 2개 병합
kospi = pd.Series([1915, 1961, 2026, 2467, 2041],
                  index = [2014, 2015, 2016, 2017, 2018], name = 'KOSPI')
kosdaq = pd.Series([542, 682, 631, 798, 675],
                  index = [2014, 2015, 2016, 2017, 2018], name = 'KOSDAQ')
df = pd.DataFrame({kospi.name: kospi, kosdaq.name: kosdaq})

#list 이용

for row in df.itertuples(name='KRX'):
    print(row)

for row in df.itertuples():
    print(row[0], row[1], row[2])
