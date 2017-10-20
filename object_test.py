#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# Author: Wang Wentao
# Created on 2017-08-13 14:55:00
import copy
from io import BytesIO
from urllib.parse import urlparse,parse_qs

import requests
from PIL import Image
from bs4 import BeautifulSoup

class Systerm(object):
	"""docstring for Syshandler"""
	def __init__(self, username='zhangqian77', departid='11a0271', password='et3YzxYGJfhigS2oi+dh/5J/3WU='):
		self.username = username
		self.departid = departid
		self.password = password
		self.urls = {}
		requests.packages.urllib3.disable_warnings()
		self.session = requests.Session()

	def GetRandomImage(self):
		################################
		#获取网站验证码并返回random_code
		################################
		PAYLOAD_IMAGE = {
		'mode':'validate',
		'width':'60',
		'height':'20'}
		r = self.session.get(
			'https://123.125.98.209/image',
			params = PAYLOAD_IMAGE,
        	verify=False)
		i = Image.open(BytesIO(r.content))
		i.show()
		self.random_code = input('test:')

	def LoginSystem(self):
    	################################
    	#登陆网站，上传用户名密码，获取BSS_ESS COOKIES 
    	################################
		DATA_LOGINSYS = {
    		'service':'direct/1/LoginProxy/$Form',
    		'sp':'S0',
    		'Form0':'ACTION_MODE,STAFF_ID,LOGIN_PASSWORD,NEED_SMS_VERIFY,SUBSYS_CODE,LOGIN_TYPE,authDomainType,soap,menuId,error,authType,authSys,LOGIN_PROVINCE_CODE,VERIFY_CODE,WHITE_LIST_LOGIN,IPASS_SERVICE_URL,IPASS_CHECK_MESSAGE,IPASS_LOGIN_PROVINCE,SIGNATURE_CODE,SIGNATURE_DATA,IPASS_LOGIN,IPASS_ACTIVATE,NEED_INSTALL_CERT,IPASS_INSTALL_RESULT,IPASS_INSTALL_MESSAGE,IPASS_LOGINOUT_DOMAIN,btnProxyLogin',
    		'STAFF_ID':self.username,
    		'LOGIN_PASSWORD':self.password,
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
    		'VERIFY_CODE':self.random_code,
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
		self.session.post(
			'https://123.125.98.209/essframe',
             headers = {'Referer': 'https://123.125.98.209/essframe?service=page/LoginProxy&login_type=redirectLogin'},
             data = DATA_LOGINSYS,
             verify=False)

	def FindService(self):
		################################
    	#获取各个服务登陆细节
    	################################
		dict_userid = {
		'staffId':self.username,
		'departId':self.departid,
    	'subSysCode':'BSS',
    	'eparchyCode':'0010'
    	}
		page = self.session.get(
			'https://123.125.98.209/essframe?service=page/Nav&STAFF_ID=' + self.username,
			headers = {'Accept': 'application/x-ms-application, image/jpeg, application/xaml+xml, image/gif, image/pjpeg, application/x-ms-xbap, */*'},
            cookies = {'LOGIN_SUBSYS_CODEBSS':'CRM'},
            verify=False)
		soup = BeautifulSoup(page.text,'html.parser')
		for tag in soup.findAll(menuid=True):
			try:
				url = tag['onclick']
				url = url.split(';')[1].split('\'')[1]
				url_params = parse_qs(urlparse(url).query,True)
				for key, value in url_params.items():
					url_params[key] = value[0]
				url_params.update(dict_userid)
				self.urls[tag.string]=url_params
			except:
				self.urls[tag.string]={}
	
	def LoginService(self, url='stat', title='ESS业务受理明细查询'):
		self.session.get(
			'https://123.125.98.209/'+url,
			params=self.urls[title], 
			headers={'Referer':'https://123.125.98.209/essframe?service=page/'}, 
			verify=False)
	def Login(self):
		self.GetRandomImage()
		self.LoginSystem()
		self.FindService()

	def init_Spider(self):
		self.LoginService('stat', 'ESS业务受理明细查询')
		Spider.session_stat = copy.deepcopy(self.session)
		self.LoginService('custserv','局方停机')
		Spider.session_custserv = copy.deepcopy(self.session)
		


	def GetDepartSalesOrders(self, agent_departid, search_date):
		DATA = {
		'service':'direct/1/reportDay/frmReportSearch',
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
		'$FormConditional$5':'T',
		'$FormConditional$4':'F',
		'$FormConditional$6':'F',
		'$FormConditional$7':'T',
		'$FormConditional$8':'F',
		'$FormConditional$9':'F',
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
		#'cond_CONDITION':'查询时间：2017-07-22  地市：北京市  '\#'区县：二区  部门：伟龙智圣（北京）科技发展有限公司（二里庄小区南门）沃家厅  |员工：全部  专业网别：全部  业务大类：全部  业务受理类型：全部'.encode('GBK'),
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
		'cond_CON_DEPART_CODE':agent_departid,
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
		'cond_QUERY_DATE':search_date,
		'cond_CON_EPARCHY_CODE':'0010',
		'cond_CON_CITY_CODE':'225',
		'cond_CON_DEPART_NAME':'伟龙智圣（北京）科技发展有限公司（二里庄小区南门）沃家厅'.encode('GBK'),
		'cond_CON_STAFF_CODE':'%',
		'cond_ESS_NET_KIND':'%',
		'cond_ESS_BUSI_FLAG':'%',
		'cond_TRADE_TYPE_CODE':'%',
		}

		r = self.session.post(
			'https://123.125.98.209/stat',
			headers = {'Referer': 'https://123.125.98.209/stat'},
			data = DATA
			)
		self.orders = []

		soup = BeautifulSoup(r.text,'lxml')
		html = soup.find(attrs = {'name':'content'})['value']
		data = BeautifulSoup(html,'lxml')
		for rows in data.find_all(id='datarow'):
			title_list = ['ID','数据来源','业务类型','营业厅','营业员','网别','订单流水号','产品','受理时间','用户号码','客户名称','订单返销状态','备注']
			title_list.reverse()
			detail = {}
			for content in rows.contents:
				detail[title_list.pop()] = content.text
			my_order = Order(**detail)
			self.orders.append(my_order)
		return self.orders

	def GetAgentOrdersByDates(self, begin_date, end_date, agent_departid):
		pass

		
class SpiderManager(object):
	"""docstring for SpiderManager"""
	def __init__(self, 
		agents=['11b2821','11b27g2','11b22kt','11b1xhs','11b1web','11b1wc7','11b1wc5','11b1ska','11b1sk9','11b1scq',
		'11b1p97','11b1iho','11b1g9r','11b1fmw','11b1dzj','11b1dz7','11b1dz5','11b1cul','11b13ds','11b0y2o','11b0xns',
		'11b0wqy','11b0jl9','11b0d0w','11b0cir','11b0ayi','11b0ag5','11b082z','11b03ye','11a2570','11b0bon','11b13rr'], 
		):
		self.agents = agents


class Spider(object):
	
	def GetDepartSalesOrders(self, agent_departid, search_date):
		DATA = {
		'service':'direct/1/reportDay/frmReportSearch',
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
		'$FormConditional$5':'T',
		'$FormConditional$4':'F',
		'$FormConditional$6':'F',
		'$FormConditional$7':'T',
		'$FormConditional$8':'F',
		'$FormConditional$9':'F',
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
		#'cond_CONDITION':'查询时间：2017-07-22  地市：北京市  '\#'区县：二区  部门：伟龙智圣（北京）科技发展有限公司（二里庄小区南门）沃家厅  |员工：全部  专业网别：全部  业务大类：全部  业务受理类型：全部'.encode('GBK'),
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
		'cond_CON_DEPART_CODE':agent_departid,
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
		'cond_QUERY_DATE':search_date,
		'cond_CON_EPARCHY_CODE':'0010',
		'cond_CON_CITY_CODE':'225',
		'cond_CON_DEPART_NAME':'伟龙智圣（北京）科技发展有限公司（二里庄小区南门）沃家厅'.encode('GBK'),
		'cond_CON_STAFF_CODE':'%',
		'cond_ESS_NET_KIND':'%',
		'cond_ESS_BUSI_FLAG':'%',
		'cond_TRADE_TYPE_CODE':'%',
		}

		r = self.session.post(
			'https://123.125.98.209/stat',
			headers = {'Referer': 'https://123.125.98.209/stat'},
			data = DATA
			)
		self.orders = []

		soup = BeautifulSoup(r.text,'lxml')
		html = soup.find(attrs = {'name':'content'})['value']
		data = BeautifulSoup(html,'lxml')
		for rows in data.find_all(id='datarow'):
			title_list = ['ID','数据来源','业务类型','营业厅','营业员','网别','订单流水号','产品','受理时间','用户号码','客户名称','订单返销状态','备注']
			title_list.reverse()
			detail = {}
			for content in rows.contents:
				detail[title_list.pop()] = content.text
			my_order = Order(**detail)
			self.orders.append(my_order)
		return self.orders

	
class Order(object):
	def __init__(self, *args, **kw):
		if '订单流水号' in kw:
			self.id = kw['订单流水号']

		if '用户号码' in kw:
			self.number = kw['用户号码']

		if '客户名称' in kw:
			self.custName = kw['客户名称']

		if '受理时间' in kw:
			self.date = kw['受理时间']

		if '产品' in kw:
			self.product = kw['产品']

		if '营业厅' in kw:
			self.agent = kw['营业厅']



	def print(self):
		print('用户号码 : %s , 产品 : %s \n营业厅 : %s , 受理时间 : %s' %(self.number, self.product, self.agent, self.date))

	def GetcustomerInfoByNum(self):
		DATA = {
                "SERIAL_NUMBER":str(self.number),
                "_rightCode":"csForceModifyStopTrade",
                "service":"direct/1/personalserv.changesvcstate.changesvcstate/$MobTrade.$Form$0",
                "_tradeBase":"H4sIAAAAAAAAAFvzloG1fAJDX7VSSJCji2t8SGSAa7yzv4urkpWhsZmOUmaeb35KqjMQK1kpGSjpKAX5h4a4xrsGOAY5e0QCxZ72TH+ya83THU0gOU93jxCobqXkYrf8ouRUoPbMtMrgkvyCkKJEoCk6UIs8XYBq4LzgEMeQ0GCgSGZeZolSLQDy/uOZlgAAAA==",
                "Form0":"ORDER_MGR,RElA_TRADE_ID,ORDER_TYPE,SUPPORT_TAG,COMM_SHARE_NBR_STRING,AC_INFOS,FORGIFT_USER_ID,QUERY_ACCOUNT_ID,_rightCode,inModeCode,NET_TYPE_CODE,SERIAL_NUMBER,subQueryTrade",
                "sp":"S0",
                "subQueryTrade":"%B2%E9%D1%AF",
                "inModeCode":"0"}
		r = self.session.post(
                'https://123.125.98.209/custserv',
                data = DATA,
                verify=False,
                headers = {'Referer': 'https://123.125.98.209/custserv'}
                )
		soup = BeautifulSoup(r.text,'html5lib')
		try:
			#print('try')
			person_id = soup.find(id='PSPT_ID')['value']
			person_name = soup.find(id='CUST_NAME')['value']
			person_address = soup.find(id='PSPT_ADDR')['value']
		except:
			person_id = person_name = person_address = '客户身份获取错误'
		finally:
			return Customer(person_name, person_id, person_address)


class Customer(object):
	"""docstring for Customer"""
	def __init__(self, person_name, person_id, person_address):
		self.name = person_name
		self.id = person_id
		self.address = person_address

	def print(self):
		print('姓名： %s \n 身份证号： %s \n 身份证地址： %s' % (self.name, self.id, self.address))

		
		

if __name__ == '__main__':
	sys = Systerm()
	spider_manager = sys.Create_SpiderManager()
	print(spider_manager.session_stat)
	print(spider_manager.session_custserv)
	



