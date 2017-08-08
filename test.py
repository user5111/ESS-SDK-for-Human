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
#depart_ids = ['11b2821','11b27g2','11b22kt','11b1xhs','11b1web','11b1wc7','11b1wc5','11b1ska','11b1sk9','11b1scq','11b1p97','11b1iho','11b1g9r','11b1fmw','11b1dzj','11b1dz7','11b1dz5','11b1cul','11b13ds','11b0y2o','11b0xns','11b0wqy','11b0jl9','11b0d0w','11b0cir','11b0ayi','11b0ag5','11b082z','11b03ye','11a2570','11b0bon','11b13rr']
depart_ids = ['11b2821','11b27g2','11b22kt']
begin_date = '2017-08-01'
end_date = '2017-08-06'
wb = Workbook()
dest_filename = '/Users/wangwentao/Desktop/test.xlsx'
ws1 = wb.active
ws1.title = "ESS"
requests.packages.urllib3.disable_warnings()

session = requests.Session()
        
urls = login.LoginEssSystem(USERNAME,DEPARTID,PASSWORD,session)
login.LoginService(urls, 'ESS业务受理明细查询','stat', session)
for depart_id in depart_ids:
        begin = datetime.now()
        sales_details = departinfo.getSalesDetailsByDate(begin_date, end_date, depart_id, session, urls)
        end = datetime.now()
        print('run time: '+ str(end - begin))
        for sales_detail in sales_details:
            ws1.append(list(value for (key,value) in sales_detail.items()))
wb.save(filename = dest_filename)

