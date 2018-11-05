# -*- coding: utf-8 -*-
import pandas as pd
DataFrame = pd.read_csv('ExpensesRecord.csv')
DataFrame["單價"]=DataFrame["支出金額"]/DataFrame["數量"]
print(DataFrame[["說明","數量","支出金額","單價"]] )


