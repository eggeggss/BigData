#!/usr/bin/env python
# -*- coding=utf-8 -*-
__author__ = "Powen Ko, www.powenko.com"
import pandas as pd
df = pd.read_csv('ExpensesRecord.csv')
print(df.head(5) )
df.to_csv("test.csv")
