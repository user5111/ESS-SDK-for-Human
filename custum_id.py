#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# Author: Wang Wentao
# Created on 2017-07-24 16:00:00

import requests

def GetCustomerIdByNumber(urls, number, session):
	r = session.post('https://123.125.98.209/custserv',data=urls['局方停机'], headers={'Referer':'https://123.125.98.209/essframe?service=page/Sidebar'}, verify=False)
	