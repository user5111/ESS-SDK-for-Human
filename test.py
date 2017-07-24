import login
import requests


USERNAME = 'wangping80'
DEPARTID = '11a0271'
PASSWORD = 'aUiJOHzTKG1V/avl/jU3gMdE+Ns='


session = requests.Session()


urls = login.LoginEssSystem(USERNAME,DEPARTID,PASSWORD,session)
r = session.post('https://123.125.98.209/custserv',data=urls['局方停机'], headers={'Referer':'https://123.125.98.209/essframe?service=page/Sidebar'}, verify=False)
	