#!/usr/bin/env
# -*- coding: utf-8 -*-    
__author__ = "Powen Ko, www.powenko.com"
import pandas as pd
#import pandas.io.data as web
from pandas_datareader import data, wb
import pandas_datareader.data as web

import datetime


import fix_yahoo_finance as yf
yf.pdr_override() # <== that's all it takes :-)

# download dataframe
#df = web.get_data_yahoo("AAPL", start="2018-01-01", end="2018-04-30")
df = web.get_data_yahoo("2330.TW", start="2018-01-01", end="2018-07-17")



#下載資料起始日與股票代號
start = datetime.datetime(2016,4,1)
end = datetime.datetime(2016,4,19)
#df=web.DataReader('2330.tw','yahoo',start,end)

#日股價資料寫入excel檔



writer=pd.ExcelWriter('2330TW.xlsx')
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