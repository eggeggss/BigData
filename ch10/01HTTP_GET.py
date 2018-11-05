# -*- coding: UTF-8 -*-
__author__ = "Powen Ko, www.powenko.com"
import sys 
try:
    import urllib2 as httplib   # 2.x
except Exception:
    import urllib.request as httplib  # 3.x
try:
    url="http://www.powenko.com/download_release/get.php?name=powenko"
    #url="http://data.taipei/opendata/datalist/datasetMeta/download?id=5bc82dc7-f2a2-4351-abc8-c09c8a8d7529&rid=1f1aaba5-616a-4a33-867d-878142cac5c4"
    #url="http://data.taipei/opendata/datalist/datasetMeta/download?id=5a911ea5-1694-4301-808e-e1780d971611&rid=da7a8c16-9a47-4671-a8aa-8bf75030dfc7"
    req=httplib.Request(url)
    reponse = httplib.urlopen(req)
    if reponse.code==200:
        if (sys.version_info > (3, 0)):
            contents=reponse.read().decode(reponse.headers.get_content_charset())
        else:  
        	contents=reponse.read()   
        print(contents)
except:
    print("error")   