
import requests
from io import BytesIO
from PIL import Image
from bs4 import BeautifulSoup


import login
import custinfo
import departinfo



USERNAME = 'zhangqian77'
DEPARTID = '11a0271'
PASSWORD = 'et3YzxYGJfhigS2oi+dh/5J/3WU='
numbers = ['13120273099','13120273199','1312111111']
depart_id = '11b1scq'
search_date = '2017-07-30'

session = requests.Session()
urls = login.LoginEssSystem(USERNAME,DEPARTID,PASSWORD,session)
login.LoginService(urls, 'ESS业务受理明细查询','stat', session)
sales_details = departinfo.getDepartSalesDetails(depart_id, search_date, session)

def sales_details_filter(sales_detail):
    return sales_detail['业务类型'] == '开户' or  sales_detail['业务类型'] == '用户资料返档'
sales_details = list(filter(sales_details_filter,sales_details))

for sales_detail in sales_details:
    print(sales_detail['用户号码'])
    login.LoginService(urls, '局方停机','custserv', session)
    custinfos = custinfo.GetCustinfoByNum(sales_detail['用户号码'], session)
    print(custinfos)

