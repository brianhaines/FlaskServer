#!/usr/bin/env python3
import os
import mysql.connector as mysql
from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash
import json
from datetime import datetime as dt

#This is a text file with my db username and PW etc.
#params = open('dbparams.txt').read()
#params = open('/home/ubuntu/Yahoo/dbparams.txt').read()
#params =  params.split(',')


# create our little application :)
app = Flask(__name__)

<<<<<<< HEAD
db = mysql.connect(user=os.environ.get('dbUser'),password=os.environ.get('dbPW'),host=os.environ.get('dbHost'),database=os.environ.get('dbName'))
	
=======
>>>>>>> d9a2bc6ac57d3370986f1bc0243a0aeaee0de6b2

@app.route('/')
def hello_world():
	return 'To get some price history, add /prices/ to this address. Also add a ticker and the number of records you need. eg /prices/XOM&360'

@app.route('/prices/<stkReq>')
def stock_tip(stkReq):
	
	try:
		s = stkReq.split('&')
		tkr = s[0]
		n = int(s[1])
	except:
		n=120

<<<<<<< HEAD
=======
	
	db = mysql.connect(user=os.environ.get('dbUser'),password=os.environ.get('dbPW'),host=os.environ.get('dbHost'),database=os.environ.get('dbName'))
>>>>>>> d9a2bc6ac57d3370986f1bc0243a0aeaee0de6b2
	cursor = db.cursor()

	cursor.execute('''SELECT qDate, tBucket, avg(tPrice),max(tPrice),min(tPrice) FROM livePrices WHERE Ticker=%s AND tPrice!='Null' GROUP BY qDate, tBucket ORDER BY qDate DESC,tBucket DESC LIMIT %s''',(tkr,n))

	outPut=[]
	for each in cursor:
		outPut.append([str(each[0]),str(each[1]),round(each[2],2),round(each[3],2),round(each[4],2)])

	dats = {'Ticker':tkr,'Prices':outPut}
<<<<<<< HEAD
	cursor.close()
=======
>>>>>>> d9a2bc6ac57d3370986f1bc0243a0aeaee0de6b2
	return json.dumps(dats,separators=(',', ':'))


@app.route('/keystats/<stkReq>')
def stock_stats(stkReq):
	return "YEAH BUDDY! "+stkReq


if __name__ == '__main__':
	port=int(os.environ.get('PORT', 5000))
	app.run(port=port)

