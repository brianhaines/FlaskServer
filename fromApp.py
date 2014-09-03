import requests
#	from urllib.request import urlopen
import json

# url = 'http://finance.yahoo.com/q/ks?s=%s+Key+Statistics' %tkr
# ksPage = urlopen(url)

# ?url = 'http://streamerapi.finance.yahoo.com/streamer/1.0?s=%s&k=%s&r=0&callback=parent.yfs_u1f&mktmcb=parent.yfs_mktmcb&gencallback=parent.yfs_gencb' % (tickerStr,fieldsStr)
url = 'http://yahooserver.herokuapp.com/prices/SPY&500'
r = requests.get(url).json()
# j = r.json()

print(r['Ticker'])

for each in r['Prices']:
	print(each[1],' ',each[3])

# for 
# print()