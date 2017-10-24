#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# Author: Wang Wentao
# Created on 2017-10-18 13:42:00
from datetime import datetime ,timedelta

import requests
from io import BytesIO
from PIL import Image
from bs4 import BeautifulSoup
from openpyxl import load_workbook


import login
import custinfo
import departinfo


USERNAME = 'zhangqian77'  
DEPARTID = '11a0271'
PASSWORD = 'et3YzxYGJfhigS2oi+dh/5J/3WU='
requests.packages.urllib3.disable_warnings()

def handle(tradeid):
    try:
        for data in tradeid.find_all('data'):
            if data['tradeTypeCode'] == '10' or data['tradeTypeCode'] == '12':
                tradeId = data['tradeId']
        return tradeId
    except:
        return 'ERROR'
session = requests.Session()
urls = login.LoginEssSystem(USERNAME,DEPARTID,PASSWORD,session)
wb = load_workbook(filename = '/Users/wangwentao/Desktop/target1.xlsx')
ws = wb['Sheet3']

for row in ws:
    number = row[6].value
    print(number)
    login.LoginService(urls, '用户资料综合查询','custserv', session)
    custinfos = custinfo.GetCustinfoByNum(number, session)
    id_photo_status = custinfo.GetCustIdPhotoById(custinfos['cust_id'],session)
    login.LoginService(urls, '用户照片查询','custserv', session)
    tradeid = custinfo.GetTradeIdPro(number,custinfos['open_date'], session)
    print(tradeid)
    live_photo_status = custinfo.GetCustLivePhotoByTradeId(tradeid, session)
    row[8].value = id_photo_status
    row[9].value = live_photo_status
wb.save('/Users/wangwentao/Desktop/target.xlsx')
    

    
    




