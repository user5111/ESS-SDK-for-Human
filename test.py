
import requests
from io import BytesIO
from PIL import Image
from bs4 import BeautifulSoup


import login
import custinfo


USERNAME = 'wangping80'
DEPARTID = '11a0271'
PASSWORD = 'aUiJOHzTKG1V/avl/jU3gMdE+Ns='
numbers = ['13120273099','13120273199','1312111111']

session = requests.Session()

urls = login.LoginEssSystem(USERNAME, DEPARTID, PASSWORD, session)
login.LoginService(urls, '局方停机', session)
for number in numbers:
    custinfos = custinfo.GetCustinfoByNum(number, session)
    DATA = {'PSPT_ID':custinfos['cust_id'],'CUSTNAME':custinfos['cust_name'],'globalPageName':'popupdialog.PersonCardReaderSX'}
    r = session.post(
        'https://123.125.98.209/custserv',
        params = {'service':'swallow/popupdialog.PersonCardReaderSX/checkPsptInfo/1'},
        headers = {'Referer': 'https://123.125.98.209/custserv'},
        data = DATA,
        verify = False
        )
    image = Image,open(BytesIO(r.content))
    image.show()


    print(custinfos)
	
