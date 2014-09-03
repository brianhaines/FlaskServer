import mysql.connector as mysql
from datetime import datetime
from datetime import time

#This is a text file with my db username and PW etc.
params = open('dbparams.txt').read()
#params = open('/home/ubuntu/Yahoo/dbparams.txt').read()

params =  params.split(',')


ticker = 'XOM'
qDate = '2014-09-02'

#Connect to MySQL database
db = mysql.connect(user=params[0],password=params[1],host=params[2],database=params[3])
cursor = db.cursor()
tkr = ticker
cursor.execute('''SELECT tBucket, avg(tPrice) FROM livePrices WHERE Ticker=%s AND qDate='2014-09-02' AND tPrice!='Null' GROUP BY tBucket ORDER BY qTime DESC LIMIT 1''',(tkr,))


for each in cursor:
	outPut = [str(each[0]),each[1]]

print(outPut)