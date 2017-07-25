
import requests
from bs4 import BeautifulSoup

import login
import custinfo


USERNAME = 'wangping80'
DEPARTID = '11a0271'
PASSWORD = 'aUiJOHzTKG1V/avl/jU3gMdE+Ns='
numbers = ['15611691902','13120273099','13120273199','1312111111']

session = requests.Session()

urls = login.LoginEssSystem(USERNAME, DEPARTID, PASSWORD, session)
login.LoginService(urls, '局方停机', session)
for number in numbers:
    custinfos = custinfo.GetCustinfoByNum(number, session)
    print(custinfos)
	
