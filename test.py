
import requests
from io import BytesIO
from PIL import Image
from bs4 import BeautifulSoup


import login
import custinfo


USERNAME = 'zhangqian77'
DEPARTID = '11a0271'
PASSWORD = 'et3YzxYGJfhigS2oi+dh/5J/3WU='
numbers = ['13120273099','13120273199','1312111111']

session = requests.Session()

urls = login.LoginEssSystem(USERNAME, DEPARTID, PASSWORD, session)
login.LoginService(urls, 'ESS业务受理明细查询', session)
session.post('https://123.125.98.209/stat',
             headers = {'Referer': 'https://123.125.98.209/stat'},
             data = {'service':'direct/1/reportDay/frmReportSearch',
'sp':'S0',
'Form0':'$FormConditional,cond_CON_EPARCHY_CODE,$FormConditional$0,cond_CON_CITY_CODE,$FormConditional$1,$FormConditional$2,$FormConditional$3,'\
          '$FormConditional$4,$FormConditional$5,cond_CON_DEPART_NAME,$FormConditional$6,$FormConditional$7,cond_CON_STAFF_CODE,$FormConditional$8,$FormConditional$9,'\
          '$FormConditional$10,$FormConditional$11,$FormConditional$12,$FormConditional$13,cond_ESS_NET_KIND,$FormConditional$14,$FormConditional$15,cond_ESS_BUSI_FLAG,'\
          '$FormConditional$16,cond_TRADE_TYPE_CODE,$FormConditional$17,$FormConditional$18,$FormConditional$19,$FormConditional$20,$FormConditional$21,$FormConditional$22,'\
          '$FormConditional$23,$FormConditional$24,$FormConditional$25,$FormConditional$26,$FormConditional$27,$FormConditional$28,$FormConditional$29',
'$FormConditional':'T',
'$FormConditional$0':'T',
'$FormConditional$1':'T',
'$FormConditional$2':'F',
'$FormConditional$3':'F',
'$FormConditional$4':'F',
'$FormConditional$5':'T',
'$FormConditional$6':'T',#'F',
'$FormConditional$7':'T',
'$FormConditional$8':'T',#'F',
'$FormConditional$9':'T',#'F',
'$FormConditional$10':'F',
'$FormConditional$11':'F',
'$FormConditional$12':'F',
'$FormConditional$13':'T',
'$FormConditional$14':'F',
'$FormConditional$15':'T',
'$FormConditional$16':'T',
'$FormConditional$17':'F',
'$FormConditional$18':'F',
'$FormConditional$19':'F',
'$FormConditional$20':'F',
'$FormConditional$21':'F',
'$FormConditional$22':'F',
'$FormConditional$23':'F',
'$FormConditional$24':'F',
'$FormConditional$25':'F',
'$FormConditional$26':'F',
'$FormConditional$27':'F',
'$FormConditional$28':'F',
'$FormConditional$29':'F',
'cond_QUERY_FLAG':'Y',
'cond_QUERY_TYPE':'VIEW',
#'cond_CONDITION':'查询时间：2017-07-22  地市：北京市  '\
#'区县：二区  部门：伟龙智圣（北京）科技发展有限公司（二里庄小区南门）沃家厅  |员工：全部  专业网别：全部  业务大类：全部  业务受理类型：全部'.encode('GBK'),
'cond_CURRPAGE':'1',
'cond_TOTALPAGE':'1',
'cond_COUNTS':'20',
#'cond_GROUP_FILED':'',
#'cond_FILTER_FILED':'',
#'cond_REPLACE_TAG':'',
'RIGHT':'3',
'cond_REPORT_ID':'STAT_TRAD_004',
'cond_REPORT_NAME':'业务量明细表'.encode('GBK'),
'cond_DATE_TAG':'0',
#'cond_PRODUCT_ID':'',
#'cond_BRAND_CODE':'',
'cond_CONDITION_FLAG':'21',
'cond_CON_DEPART_CODE':'11b1scq',
'cond_CON_DEPART_CODE_PROV':'%',
#'cond_NET_TYPE_CODE':'',
'cond_ESS_WITHDRAVALS':'0',
'cond_ESS_OTHER_PAY':'0',
'cond_CLCT_FLAG':'0',
#'cond_OPERATE_NAME':'',
'cond_PROVINCE_CODE':'11',
'cond_CLCT_RIGHT_CODE':'',
'cond_CON_FLITER_FLAG':'3',
'cond_LOGIN_STAFF_ID':'zhangqian77',
'cond_CLCT_TYPE':'0',
'cond_QUERY_DATE':'2017-07-22',
'cond_CON_EPARCHY_CODE':'0010',
'cond_CON_CITY_CODE':'225',
'cond_CON_DEPART_NAME':'伟龙智圣（北京）科技发展有限公司（二里庄小区南门）沃家厅'.encode('GBK'),
'cond_CON_STAFF_CODE':'%',
'cond_ESS_NET_KIND':'%',
'cond_ESS_BUSI_FLAG':'%',
'cond_TRADE_TYPE_CODE':'%',
                     }
    )


	
