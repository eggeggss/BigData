#!/usr/bin/env
# -*- coding: utf-8 -*-    
__author__ = "Powen Ko, www.powenko.com"


import pandas as pd
pd.core.common.is_list_like = pd.api.types.is_list_like

from pandas_datareader import data, wb
import pandas_datareader.data as web


import fix_yahoo_finance as yf
yf.pdr_override()



df = web.get_data_yahoo("AAPL", start="2018-01-01", end="2018-08-20")
print(df.head())
writer=pd.ExcelWriter('AAPL.xlsx')
df.to_excel(writer,'AAPL')
