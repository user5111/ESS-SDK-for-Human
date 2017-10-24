#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# Author: Wang Wentao
# Created on 2017-07-24 16:00:00

from io import BytesIO
from PIL import Image
from datetime import datetime, date, timedelta

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
        soup = BeautifulSoup(r.text,'html5lib')
        try:
                custinfo['cust_id'] = soup.find(id='PSPT_ID')['value']
                custinfo['cust_name'] = soup.find(id='CUST_NAME')['value']
                custinfo['open_date'] = soup.find(id='OPEN_DATE')['value']
                #print(custinfo)
                return custinfo
        except Exception as e:
                return ERROR_TAG


def GetCustinfoByNumPro(number,session):
    DATA = {
        'sp':'S0',
        'QUERY_TYPE':'on',
        'autoSearch':'no',
        'service':'direct/1/personalserv.integratequerytrade.IntegrateQueryTrade/workarea',
        'cond_SERIAL_NUMBER':str(number),
        'importTag':' 1',
        'ACCPROVICE_ID':' 0011',
        'PROVICE_ID':'0011',
        'CUR_PROVINCE':'  0010',
        'N6_15906_TAGCODE':'0',
        'N3_11486_TAG_CODE':'0',
        'CS_TAG_101075':'0',
        'SMS_NUMBER_TAG_1':'0',
        'CS_CONTRAL_TAG':'0',
        'cond_QUERY_METHOD':'0',
        'SD_SHOW_TAGCODE':'',
        'QC_106655_TAG':'0',
        'N6_17426_USE_TAG':'0',
        'allInfo':'{}',
        '_BoInfo':'{"BO_IOM_QUERYWO_URL":"","BO_SYS_NAME":"DT","BO_PASSWORD":"gc","BO_USERNAME":"gc"}',
        'tabSetList':'[{"PARA_CODE3":"","PARA_CODE2":"1","PARAM_CODE":"YH-XX","PARA_CODE1":"1","PARAM_NAME":"用户信息"},{"PARA_CODE3":"getUserAttrInfo","PARA_CODE2":"1","PARAM_CODE":"YH-SX-XX","PARA_CODE1":"2","PARAM_NAME":"用户属性信息"},{"PARA_CODE3":"","PARA_CODE2":"1","PARAM_CODE":"KH-XX","PARA_CODE1":"3","PARAM_NAME":"客户信息"},{"PARA_CODE3":"getInfo4","PARA_CODE2":"1","PARAM_CODE":"ZH-XX","PARA_CODE1":"4","PARAM_NAME":"帐户信息"},{"PARA_CODE3":"","PARA_CODE2":"1","PARAM_CODE":"CP-XX","PARA_CODE1":"5","PARAM_NAME":"产品信息"},{"PARA_CODE3":"getInfo6","PARA_CODE2":"1","PARAM_CODE":"FW-XX","PARA_CODE1":"6","PARAM_NAME":"服务信息"},{"PARA_CODE3":"getInfo7","PARA_CODE2":"1","PARAM_CODE":"UH-XX","PARA_CODE1":"7","PARAM_NAME":"优惠信息"},{"PARA_CODE3":"getInfo7","PARA_CODE2":"1","PARAM_CODE":"ZY-XX","PARA_CODE1":"8","PARAM_NAME":"资源信息"},{"PARA_CODE3":"getInfo9","PARA_CODE2":"1","PARAM_CODE":"YH-GX-XX","PARA_CODE1":"9","PARAM_NAME":"用户关系信息"},{"PARA_CODE3":"getInfo10","PARA_CODE2":"1","PARAM_CODE":"UJ-XX","PARA_CODE1":"10","PARAM_NAME":"邮寄信息"},{"PARA_CODE3":"getInfo11","PARA_CODE2":"1","PARAM_CODE":"YJ-XX","PARA_CODE1":"11","PARAM_NAME":"押金信息"},{"PARA_CODE3":"getInfo12","PARA_CODE2":"1","PARAM_CODE":"JF-XX","PARA_CODE1":"12","PARAM_NAME":"积分信息"},{"PARA_CODE3":"getInfo13","PARA_CODE2":"1","PARAM_CODE":"GJ-XX","PARA_CODE1":"13","PARAM_NAME":"购机基本信息"},{"PARA_CODE3":"getInfo14","PARA_CODE2":"1","PARAM_CODE":"GJ-JB","PARA_CODE1":"14","PARAM_NAME":"购机其他信息"},{"PARA_CODE3":"","PARA_CODE2":"1","PARAM_CODE":"SP-XX","PARA_CODE1":"15","PARAM_NAME":"SP信息"},{"PARA_CODE3":"","PARA_CODE2":"1","PARAM_CODE":"HD-XX","PARA_CODE1":"16","PARAM_NAME":"活动信息"},{"PARA_CODE3":"","PARA_CODE2":"1","PARAM_CODE":"YH-SB-XX","PARA_CODE1":"17","PARAM_NAME":"用户设备信息"},{"PARA_CODE3":"","PARA_CODE2":"1","PARAM_CODE":"PAYRELATION-INFO","PARA_CODE1":"18","PARAM_NAME":"付费关系信息"},{"PARA_CODE3":"","PARA_CODE2":"1","PARAM_CODE":"ZH-YH-XX","PARA_CODE1":"19","PARAM_NAME":"帐户优惠信息"},{"PARA_CODE3":"","PARA_CODE2":"1","PARAM_CODE":"YH-TY-XX","PARA_CODE1":"20","PARAM_NAME":"用户体验信息"},{"PARA_CODE3":"getKXXY","PARA_CODE2":"","PARAM_CODE":"KH-XY-XX","PARA_CODE1":"21","PARAM_NAME":"客户协议信息"},{"PARA_CODE3":"","PARA_CODE2":"","PARAM_CODE":"UH-GIFT","PARA_CODE1":"22","PARAM_NAME":"用户礼品"},{"PARA_CODE3":"getInfo23","PARA_CODE2":"1","PARAM_CODE":"ENDALL-XX","PARA_CODE1":"23","PARAM_NAME":"失效服务优惠SP信息"},{"PARA_CODE3":"getInfo24","PARA_CODE2":"1","PARAM_CODE":"YYGJ-XX","PARA_CODE1":"24","PARAM_NAME":"预约购机基本信息"},{"PARA_CODE3":"getInfo25","PARA_CODE2":"1","PARAM_CODE":"RHCY_XX","PARA_CODE1":"25","PARAM_NAME":"融合用户优惠信息"},{"PARA_CODE3":"getInfo26","PARA_CODE2":"1","PARAM_CODE":"YHDB_XX","PARA_CODE1":"26","PARAM_NAME":"担保信息"},{"PARA_CODE3":"getInfo27","PARA_CODE2":"1","PARAM_CODE":"DID_XX","PARA_CODE1":"27","PARAM_NAME":"DID信息"},{"PARA_CODE3":"getInfo28","PARA_CODE2":"1","PARAM_CODE":"OCS_XX","PARA_CODE1":"28","PARAM_NAME":"OCS生命周期查询"}]'.encode('GBK'),
        'Form0':'$DateField,autoSearch,custTreaty,importTag,tabSetList,allInfo,CURRENT_BRAND,CURRENT_PRODUCT_NAME,CUR_PROVINCE,SD_SHOW_TAGCODE,N6_15906_TAGCODE,N2_QKWB,QC_106655_TAG,CS_CONTRAL_TAG,N6_17426_USE_TAG,N3_11486_TAG_CODE,SMS_NUMBER_TAG_1,SUPPORT_TAG,AC_INFOS,cond_QUERY_METHOD,cond_NET_TYPE_CODE,cond_CUST_NAME,cond_CUST_ID,cond_SERIAL_NUMBER,cond_RES_NO,_BoInfo,LAST_BRAND,LAST_PRODUCT_NAME,X_OPEN_MODE_NAME,BRAND,PRODUCT_NAME,USER_TYPE,$TextField,$TextField$0,FIRST_CALL_TIME,LAST_STOP_TIME,X_EPARCHY_NAME,CITY_NAME,USER_CALLING_AREA,X_PREPAY_TAG_NAME,X_SVCSTATE_EXPLAIN,OPEN_DATE,IN_DATE,X_ACCT_TAG_NAME,MPUTE_DATE,PRE_DESTROY_TIME,DESTROY_TIME,X_REMOVE_TAG_NAME,MPUTE_MONTH_FEE,IS_LH,CREDIT_CLASS,CREDIT_VALUE,BASIC_CREDIT_VALUE,END_DATE,DEVELOP_NO,SCORE_VALUE,INTEGRAL_USER,STAFF_NAME,CLASS_NAME,CLASS_VIP_NAME,CUST_MANAGER_ID,X_DEVELOP_STAFF_NAME,CUST_MANAGER_NUMBER,SERIAL_NUMBER,VIP_CARD_NO,ASSURE_TYPE,ASSURE_DATE,ASSURE_NAME,PARA_CODE1,PARA_CODE2,ASSURE_SERIAL_NUMBER,USER_ID,USER_NAME,CONTRACT_ID,BLACK_USER,RED_USER,$TextField$1,DOUBLE_CARD,CTAG_SET,$TextField$2,OPEN_STAFF_ID,X_OPEN_DEPART_NAME,AGENT_DEPART_ID,$TextField$3,DEVELOP_STAFF_ID_1,$TextField$4,$TextField$5,RSRV_NUM2,MOFFICE_INFO,relNameTag,$TextField$6,$TextField$7,MARKING_CODE,MARKING_TAG,MARKING_TIME,CUST_NAME,PSPT_ADDR,PSPT_TYPE,PSPT_ID,X_CUST_TYPE,$TextField$8,PSPT_END_DATE,WORK_NAME,X_CUST_STATE,REMOVE_DATE,LANGUAGE_NAME,WORK_DEPART,OPEN_LIMIT,$TextField$9,FOLK,JOB,$TextField$10,$TextField$11,PHONE,JOB_TYPE,$TextField$12,X_IN_DEPART_NAME,POST_CODE,EDUCATE_DEGREE,$TextField$13,IN_STAFF_ID,POST_ADDRESS,RELIGION_NAME,$TextField$14,$TextField$15,FAX_NBR,REVENUE_LEVEL,$TextField$16,X_SEX,EMAIL,X_MARRIAGE,$TextField$17,BIRTHDAY,CONTACT,CHARACTER_TYPE,NATIONALITY_NAME,COMMUNITY_ID,CONTACT_PHONE,WEBUSER_ID,POPULATION,CONTACT_TYPE,LOCAL_NATIVE_NAME,HOME_ADDRESS,CUST_ID,USECUST_ID,USECUST_NAME,USECUST_PSPT_TYPE,CHAT_NUMBER,WEIXIN_NUMBER,INVOICE_ACCOUNT_NUMBER,USECUST_PSPT_ID,$TextField$18,$TextField$19,$TextField$20,PAY_NAME,DEBUTY_USER_ID,PAY_MODE_CODE,DEBUTY_CODE,BANK,BANK_INNER_CODE,CONTRACT_NO,BANK_ACCT_NO,DEPOSIT_PRIOR_RULE_ID,RSRV_STR,BANK_BUSI_KIND,$TextField$21,ITEM_PRIOR_RULE_ID,$TextField$22,BANK_ACCT_NAME,$TextField$23,ACCT_ID,DISCNT_NAME,$TextField$24,$TextField$25,PROVICE_ID,CS_TAG_101075,ACCPROVICE_ID,cond_PAGE_NUM,cond_PER_PAGE_NUM,cond_CUR_NUM,userAttrInfo,titleInfo,$ListEdit,cond_TRADE_TYPE_CODE,TRADE_ID,cond_START_DATE,cond_FINISH_DATE,TRADE_STAFF_ID,X_DEVELOP_DEPART_NAME,X_DEVELOP_CITY_NAME,X_DEVELOP_EPARCHY_NAME,CANCEL_STAFF_ID,CANCEL_DEPART_ID,X_REMOVE_CITY_NAME,X_REMOVE_EPARCHY_NAME,FIELD_NAME1,OPER_FEE,ADVANCE_PAY,FOREGIFT,X_CANCEL_TAG_NAME,FIELD_NAME2,SHOW_FINISH_DATE,CHECK_TYPE_CODE,REMARK,$TextField$26,bquery,queryTradehide',
        'queryTradehide':'查询'.encode('GBK'),
        'N2_QKWB':'',
        '$teField':'',  
        'userAttrInfo':'',  
        'CURRENT_BRAND':'',
        'cond_NET_TYPE_CODE':'',
        'cond_CUST_NAME':'',
        'cond_CUST_ID':'',
        'custTreaty':'',
        'AC_INFOS':'',
        'PAY_MODE_CODE':'', 
        'SUPPORT_TAG':'',
        'cond_PAGE_NUM':'',
        'chklistframe17_hidden':'',
        'titleInfo':'',
        'TRADE_ID':'',
        'CURRENT_PRODUCT_NAME':'',
        }
    r = session.post('https://123.125.98.209/custserv', headers = {'Referer':'https://123.125.98.209/custserv'}, data = DATA)
    soup = BeautifulSoup(r.text,'lxml')
    name = soup.find(id='DEVELOP_STAFF_ID_1')['value']
    print(name)
    return name


def GetCustIdPhotoById(custid, session, fileaddr='/Users/wangwentao/Desktop/new-id/'):
        try:
                r = session.get(
                'https://123.125.98.209/custserv',
                params = {'service':'page/personalserv.print.PrintHtmlShowImage',
                          'listener':'showImage',
                          'GET_TYPE':'1',
                          'PID':custid
                          },
                headers = {'Referer': 'https://123.125.98.209/custserv',
                           'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'
                           },
                verify = False
                )
                img = Image.open(BytesIO(r.content))
                img.save(fileaddr+ custid +'.png','png')
                print(custid + ':国政通正常')
                return '通过国政通'
        except:
                print(custid + ':国政通异常')
                return '国政通异常'

def GetTradeId(serial_number, accptime, session):
        try:
                r = session.post(
                        'https://123.125.98.209/custserv',
                        data = {'accptime':accptime,
                                'SERIAL_NUMBER':serial_number,
                                'globalPageName':'personalserv.print.QueryUserPhoto'
                                },
                        headers = {'Referer': 'https://123.125.98.209/custserv',
                                   'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
                                   'x-requested-with':'XMLHttpRequest',
                                   'Accept-Encoding':'gzip,deflate',
                                   'Accept':'text/javascript, text/html, application/xml, text/xml, */*',
                                   'x-portotype-version':'1.6.1',
                                   'Cache-Control':'no-cache'
                                   },
                        params = {'service':'swallow/personalserv.print.QueryUserPhoto/afterSerialNumber/1'},
                        verify = False
                        )
                soup = BeautifulSoup(r.text,'xml')
                tradeid = soup
                return tradeid
        except:
                return tradeid

def GetTradeIdPro(serial_number, accptime, session):
        date = datetime.strptime(accptime, "%Y-%m-%d")
        start_date = (date-timedelta(days=55)).strftime('%Y-%m-%d')
        print(start_date)
        finish_date = (date+timedelta(days=35)).strftime('%Y-%m-%d')
        print(finish_date)
        try:
                r = session.post(
                        'https://123.125.98.209/custserv',
                        headers = {'Referer': 'https://123.125.98.209/custserv',
                                   'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
                                   'x-requested-with':'XMLHttpRequest',
                                   'Accept-Encoding':'gzip,deflate',
                                   'Accept':'text/javascript, text/html, application/xml, text/xml, */*',
                                   'x-portotype-version':'1.6.1',
                                   'Cache-Control':'no-cache'
                                   },
                        params = {'service':'direct/1/personalserv.integratequerytrade.QueryHTradeInfo/operationquery'},
                        data = {
                                'X_GETMODE':'1',
                                'TRADE_TYPE_CODE':'10',
                                'SEREIAL_NUMBER':serial_number,
                                'START_DATE_HIS':start_date,
                                'FINISH_DATE_HIS':finish_date,
                                'BOOK_PARAM':'N',
                                'cond_PAGE_NUM':'1',
                                'cond_PER_PAGE_MUN':'10',
                                },
                        verify = False
                        )
                soup = BeautifulSoup(r.text,'lxml')
                name = soup.find(id='theTableName')
                print(name)
        except:
                return "ERROR"
                
                
        
def GetCustLivePhotoByTradeId(TradeId, session, fileaddr='/Users/wangwentao/Desktop/new-id/'):
        try:
                r = session.post(
                        'https://123.125.98.209/custserv',
                        headers = {'Referer': 'https://123.125.98.209/'},
                        params = {'service': 'swallow/personalserv.print.QueryUserPhoto/qryPhotoInfobytrade/1'},
                        data = {
                                'accptime':'2017-05-06',
                                'TID': TradeId,
                                'syscode':'0400',
                                'globalPageName':'personalserv.print.QueryUserPhoto',
                                },
                        verify = False
                                )
                r = session.get(
                        'https://123.125.98.209/custserv',
                        params = {'service':'page/personalserv.print.QueryUserPhoto',
                                  'listener':'showImage',
                                  'num':'1',
                                  'TID':TradeId
                                  },
                        headers = {'Referer': 'https://123.125.98.209/custserv',
                                   #'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'
                                   },
                        verify = False
                        )
                img = Image.open(BytesIO(r.content))
                img.save(fileaddr+ TradeId +'.png','png')
                print(TradeId + ':现场照片正常')
                return '现场照片正常'
        except:
                print('现场照片异常')
                return '现场照片异常'


if __name__ == '__main__':
    USERNAME = 'wangping80'
    DEPARTID = '11a0271'
    PASSWORD = 'b0Xi4uh88u5eAzx/8CeDpQTDZY4='
    session = requests.Session()
    urls = login.LoginEssSystem(USERNAME,DEPARTID,PASSWORD,session)
    #login.LoginService(urls, 'ESS业务受理明细查询','stat', session)
    login.LoginService(urls, '用户资料综合查询','custserv', session)
    custinfos = GetCustinfoByNumPro('15611144389', session)
    #GetCustPhotoIdById(custinfos['cust_id'],session)
