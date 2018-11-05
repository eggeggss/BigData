#!/usr/bin/env python
# -*- coding=utf-8 -*-
__author__ = "Powen Ko, www.powenko.com"
import json
import sys 
try:
    import urllib2 as httplib   # 2.x
except Exception:
    import urllib.request as httplib  # 3.x



url="http://data.taipei/opendata/datalist/datasetMeta/download?id=ea732fb5-4bec-4be7-93f2-8ab91e74a6c6&rid=bf073841-c734-49bf-a97f-3757a6013812"
req=httplib.Request(url)
try:
    reponse = httplib.urlopen(req)
    if reponse.code==200:
        if (sys.version_info > (3, 0)):
                contents=reponse.read().decode(reponse.headers.get_content_charset())
        else:  
                contents=reponse.read()   
        data = json.loads(contents)
        for data2 in data:
            print(data2['ParkName'],data2['OpenTime'])
except:                                                                 #  處理網路連線異常
    print("error")   