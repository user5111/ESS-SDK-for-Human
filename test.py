import login
import requests


USERNAME = 'wangping80'
DEPARTID = '11a0271'
PASSWORD = 'aUiJOHzTKG1V/avl/jU3gMdE+Ns='


session = requests.Session()

headers={'Referer':'https://123.125.98.209/essframe?service=page/Sidebar'}
urls = login.LoginEssSystem(USERNAME,DEPARTID,PASSWORD,session)
r = session.get('https://123.125.98.209/custserv',params=urls['局方停机'], headers=headers, verify=False)
	
