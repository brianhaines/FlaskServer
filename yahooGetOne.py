import mysql.connector as mysql
from datetime import datetime
from datetime import time

#This is a text file with my db username and PW etc.
params = open('dbparams.txt').read()
#params = open('/home/ubuntu/Yahoo/dbparams.txt').read()

params =  params.split(',')


ticker = 'XOM'
qDate = '2014-09-03'
n=int('10')

#Connect to MySQL database
db = mysql.connect(user=params[0],password=params[1],host=params[2],database=params[3])
cursor = db.cursor()
tkr = ticker
cursor.execute('''SELECT qDate, tBucket, avg(tPrice),max(tPrice),min(tPrice) FROM livePrices WHERE Ticker=%s AND qDate=%s AND tPrice!='Null' GROUP BY tBucket ORDER BY qTime DESC LIMIT %s''',(tkr,qDate,n))

outPut=[]
for each in cursor:
	outPut.append([str(each[0]),str(each[1]),round(each[2],2),round(each[3],2),round(each[4],2)])
	

for i in outPut:
	print(i)