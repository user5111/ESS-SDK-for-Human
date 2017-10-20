#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# Author: Wang Wentao
# Created on 2017-10-18 13:42:00
from datetime import datetime ,timedelta

import requests
from io import BytesIO
from PIL import Image
from bs4 import BeautifulSoup
from openpyxl import Workbook


import login
import custinfo
import departinfo


USERNAME = 'zhangqian77'  
DEPARTID = '11a0271'
PASSWORD = 'et3YzxYGJfhigS2oi+dh/5J/3WU='

def handle(tradeid):
    for data in tradeid.find_all('data'):
        if data['tradeTypeCode'] == '10' or data['tradeTypeCode'] == '12':
            tradeId = data['tradeId']
    return tradeId
session = requests.Session()
urls = login.LoginEssSystem(USERNAME,DEPARTID,PASSWORD,session)
login.LoginService(urls, '用户资料综合查询','custserv', session)
custinfos = custinfo.GetCustinfoByNum('01013820852', session)
login.LoginService(urls, '用户照片查询','custserv', session)
tradeid = handle(custinfo.GetTradeId('01013820852','2017-05-06', session))

print(tradeid)
live_photo_status = custinfo.GetCustLivePhotoByTradeId(tradeid, session, fileaddr='C:/Users/tao/Desktop')
print(custinfos)

