#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# Author: Wang Wentao
# Created on 2017-07-18 13:00:00

from io import BytesIO
from urllib.parse import urlparse,parse_qs

import requests
from PIL import Image
from openpyxl import load_workbook
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
import matplotlib.cbook as cbook
from openpyxl.drawing.image import Image as Image2



def Init(username, departId):
    dict_userid={
    'staffId':username,
    'departId':departId,
    'subSysCode':'BSS',
    'eparchyCode':'0010'}
    return dict_userid

def GetRandomImage(session):
	################################
	#获取网站验证码并返回random_code
	################################
	PAYLOAD_IMAGE = {
		'mode':'validate',
        'width':'60',
        'height':'20'}
	r = session.get('https://123.125.98.209/image',
                       params = PAYLOAD_IMAGE,
                       verify=False)
	i = Image.open(BytesIO(r.content))
	i.show()
	random_code = input('test:')
	return random_code

def LoginSystem(username, password, random_code, session):
    ################################
    #登陆网站，上传用户名密码，获取BSS_ESS COOKIES 
    ################################
	DATA_LOGINSYS = {
    	'service':'direct/1/LoginProxy/$Form',
    	'sp':'S0',
    	'Form0':'ACTION_MODE,STAFF_ID,LOGIN_PASSWORD,NEED_SMS_VERIFY,SUBSYS_CODE,LOGIN_TYPE,authDomainType,soap,menuId,error,authType,authSys,LOGIN_PROVINCE_CODE,VERIFY_CODE,WHITE_LIST_LOGIN,IPASS_SERVICE_URL,IPASS_CHECK_MESSAGE,IPASS_LOGIN_PROVINCE,SIGNATURE_CODE,SIGNATURE_DATA,IPASS_LOGIN,IPASS_ACTIVATE,NEED_INSTALL_CERT,IPASS_INSTALL_RESULT,IPASS_INSTALL_MESSAGE,IPASS_LOGINOUT_DOMAIN,btnProxyLogin',
    	'STAFF_ID':username,
    	'LOGIN_PASSWORD':password,
    	'NEED_SMS_VERIFY':'',
    	'SUBSYS_CODE':'',
    	'LOGIN_TYPE':'redirectLogin',
    	'authDomainType':'',
    	'soap':'',
    	'menuId':'',
    	'error':'',
    	'authType':'',
    	'authSys':'',
    	'LOGIN_PROVINCE_CODE':'0011',
    	'VERIFY_CODE':random_code,
    	'WHITE_LIST_LOGIN':'',
    	'IPASS_SERVICE_URL':'http://132.35.102.170:7001/n6IpassAutherService/services/IpassAutherService',
    	'IPASS_CHECK_MESSAGE':'',
    	'IPASS_LOGIN_PROVINCE':'0091',
    	'SIGNATURE_CODE':'',
    	'SIGNATURE_DATA':'',
    	'IPASS_LOGIN':'',
    	'IPASS_ACTIVATE':'',
    	'NEED_INSTALL_CERT':'',
    	'IPASS_INSTALL_RESULT':'',
    	'IPASS_INSTALL_MESSAGE':'',
    	'IPASS_LOGINOUT_DOMAIN':'http://ess.10010.com/essframe',
    	'btnProxyLogin':'提交查询内容'.encode('GBK')
          }
	session.post(
    	'https://123.125.98.209/essframe',
       	headers = {'Referer': 'https://123.125.98.209/essframe?service=page/LoginProxy&login_type=redirectLogin'},
       	data = DATA_LOGINSYS,
       	verify=False)

def FindService(username, dict_userid, session):
    ################################
    #获取各个服务登陆细节
    ################################
    urls = {}
    page = session.get(
        'https://123.125.98.209/essframe?service=page/Nav&STAFF_ID='+username,
        headers = {'Accept': 'application/x-ms-application, image/jpeg, application/xaml+xml, image/gif, image/pjpeg, application/x-ms-xbap, */*'},
        cookies = {'LOGIN_SUBSYS_CODEBSS':'CRM'},
        verify=False)
    soup = BeautifulSoup(page.text,'html.parser')
    for tag in soup.findAll(menuid=True):
        try:
            url = tag['onclick']
            url = url.split(';')[1].split('\'')[1]
            url_params = parse_qs(urlparse(url).query,True)
            url_params.update(dict_userid)
            urls[tag.string]=url_params
        except:
            urls[tag.string]={}
    return urls





def LoginEssSystem(username, departId, password, session):
    dict_userid=Init(username,password)
    random_code = GetRandomImage(session)
    LoginSystem(username,password,random_code,session)
    page = FindService(username,dict_userid,session)
    return page



if __name__ == '__main__':
    USERNAME = 'wangping80'
    DEPARTID = '11a0271'
    PASSWORD = 'aUiJOHzTKG1V/avl/jU3gMdE+Ns='
    session = requests.Session()
    urls = LoginEssSystem(USERNAME,DEPARTID,PASSWORD,session)

