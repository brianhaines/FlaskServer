#!/usr/bin/env python3

import requests
#	from urllib.request import urlopen
import json
from collections import OrderedDict

tkr = 'SPY'
n = '360'
url = 'http://yahooserver.herokuapp.com/prices/%s&%s' % (tkr,n)
r = requests.get(url).json()
# j = r.json()

# print(r['Ticker'])

pDict=OrderedDict()

for each in r['Prices']:
	pDict[each[1]]=each[2]

# for q, r in pDict.items():
# 	print(q,r)

for q in pDict.keys():
	print(q, ' ',pDict[q])


