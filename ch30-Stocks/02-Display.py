#!/usr/bin/env
# -*- coding: utf-8 -*-
__author__ = "Powen Ko, www.powenko.com"
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#import pandas.io.data as web
"""
from pandas_datareader import data, wb
import pandas_datareader.data as web

import datetime


import fix_yahoo_finance as yf
yf.pdr_override() # <== that's all it takes :-)

# download dataframe
df = web.get_data_yahoo("AAPL", start="2017-01-01", end="2017-04-30")



#下載資料起始日與股票代號
start = datetime.datetime(2016,4,1)
end = datetime.datetime(2016,4,19)
#df=web.DataReader('2330.tw','yahoo',start,end)

#日股價資料寫入excel檔



writer=pd.ExcelWriter('AAPL.xlsx')
df.to_excel(writer,'AAPL')
workbook = writer.book
worksheet = writer.sheets['AAPL']
#畫高低圖
chart = workbook.add_chart({'type': 'stock'})
chart.add_series({'name': '=AAPL!$B$1','categories': '=AAPL!$A$2:$A$14','values': '=AAPL!$B$2:$B$14'})
chart.add_series({'name': '=AAPL!$C$1','categories': '=AAPL!$A$2:$A$14','values': '=AAPL!$C$2:$C$14'})
chart.add_series({'name': '=AAPL!$D$1','categories': '=AAPL!$A$2:$A$14','values': '=AAPL!$D$2:$D$14'})
chart.set_title ({'name': 'High-Low-Close'})
chart.set_x_axis({'name': 'Date'})
chart.set_y_axis({'name': 'Share price'})
worksheet.insert_chart('I2', chart)
writer.save()

"""

df=pd.read_excel('AAPL.xlsx')
#df.to_excel(writer,'AAPL')
print(df.head())
print(df["Date"])




ts = pd.Series(np.random.randn(1000), index=pd.date_range('1/1/2000', periods=1000))

ts = ts.cumsum()



ser = df.loc[31, :]
ts2.plot()


plt.show()


import matplotlib as mpl
mpl.rcParams['savefig.dpi'] = 120

high = df[["High", "Date"]].set_index("Date", append=True).High.unstack("Date")

plt.plot([1,2,3,4], [1,4,9,16], 'ro')
plt.axis([0, 6, 0, 20])
plt.ylabel('some numbers')
plt.xlabel('times')
plt.show()