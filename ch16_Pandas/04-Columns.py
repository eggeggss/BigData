# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
DataFrame = pd.read_csv('ExpensesRecord.csv')
print(DataFrame["說明"])
print(DataFrame[["說明","支出金額"]] )


df = pd.DataFrame({'Math': [0, 1, 2, 3, 4],'English': np.arange(0,5,1) })
print(df[["Math","English"]])


