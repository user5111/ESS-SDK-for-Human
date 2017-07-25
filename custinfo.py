#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# Author: Wang Wentao
# Created on 2017-07-24 16:00:00

import requests
from bs4 import BeautifulSoup

import login

def GetCustinfoByNum(number, session):
	custinfo = {}
	ERROR_TAG = 'NO CUSTOMER INFO FOR THIS NUMBER'
	DATA = {
    	"SERIAL_NUMBER":str(number),
    	"_rightCode":"csForceModifyStopTrade",
    	"service":"direct/1/personalserv.changesvcstate.changesvcstate/$MobTrade.$Form$0",
    	"_tradeBase":"H4sIAAAAAAAAAFvzloG1fAJDX7VSSJCji2t8SGSAa7yzv4urkpWhsZmOUmaeb35KqjMQK1kpGSjpKAX5h4a4xrsGOAY5e0QCxZ72TH+ya83THU0gOU93jxCobqXkYrf8ouRUoPbMtMrgkvyCkKJEoCk6UIs8XYBq4LzgEMeQ0GCgSGZeZolSLQDy/uOZlgAAAA==",
    	"Form0":"ORDER_MGR,RElA_TRADE_ID,ORDER_TYPE,SUPPORT_TAG,COMM_SHARE_NBR_STRING,AC_INFOS,FORGIFT_USER_ID,QUERY_ACCOUNT_ID,_rightCode,inModeCode,NET_TYPE_CODE,SERIAL_NUMBER,subQueryTrade",
    	"sp":"S0",
    	"subQueryTrade":"%B2%E9%D1%AF",
    	"inModeCode":"0"}
	r = session.post(
            'https://123.125.98.209/custserv',
            data = DATA,
            verify=False,
            headers = {'Referer': 'https://123.125.98.209/custserv'}
            )
	soup = BeautifulSoup(r.text,'lxml')
	try:
		custinfo['customer_idnum'] = soup.find(id='PSPT_ID')['value']
		custinfo['customer_name'] = soup.find(id='CUST_NAME')['value']
		custinfo['customer_address'] = soup.find(id='PSPT_ADDR')['value']
		return custinfo
	except Exception as e:
		return ERROR_TAG

if __name__ == '__main__':
    USERNAME = 'wangping80'
    DEPARTID = '11a0271'
    PASSWORD = 'aUiJOHzTKG1V/avl/jU3gMdE+Ns='
    session = requests.Session()
    urls = login.LoginEssSystem(USERNAME,DEPARTID,PASSWORD,session)
    login.LoginService(urls, '局方停机', session)
    custinfo = GetCustinfoByNum('15611144389', session)
    print(custinfo)
