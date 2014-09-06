import mysql.connector as mysql
from datetime import datetime as dt
from datetime import timedelta as td 
from time import sleep

#tickerStr = open('/home/ubuntu/Yahoo/stockList.txt').read()
#tickerStr = open('stockList.txt').read()
#tickers = tickerStr.split(',')

#This is a text file with my db username and PW etc.
params = open('dbparams.txt').read()
#params = open('/home/ubuntu/Yahoo/dbparams.txt').read()


params =  params.split(',')


ticker = 'XOM'
qDate = '2014-09-02'

#lookFor = [('XOM','2014-09-02'),('SPY','2014-09-02')]

stopTime = dt.now()+td(0,1*60)

while dt.now()<stopTime:
	#Connect to MySQL database
	db = mysql.connect(user=params[0],password=params[1],host=params[2],database=params[3])
	cursor = db.cursor()

	cursor.execute('''SELECT Ticker, qTime, tBucket, avg(tPrice),max(tPrice),min(tPrice) FROM livePrices WHERE Ticker=%s AND qDate='2014-09-02' AND tPrice!='Null' GROUP BY tBucket ORDER BY qTime DESC LIMIT 10''',(ticker,))

	print(dt.now())
	for each in cursor:
		print(each[0],each[1],each[2],"{:.2f}".format(each[3]),"{:.2f}".format(each[4]),"{:.2f}".format(each[5]))
	sleep(1)
	
	cursor.close()
	db.close()





#This is an SQL string to create a table in the database.
# cursor.execute('''CREATE TABLE IF NOT EXISTS livePrices(tickTime VARCHAR(40) NOT NULL, 
# 				Ticker VARCHAR(40), qDate DATE, qTime TIME(6),tBucket TIME(6),tPrice REAL, LastPrice REAL, bid REAL, ask REAL, 
# 				bidSize INTEGER, askSize INTEGER, volume VARCHAR(20),PRIMARY KEY (tickTime))ENGINE=InnoDB''')
# db.commit()