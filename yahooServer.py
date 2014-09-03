#!/usr/bin/env python3
import os
import mysql.connector as mysql
from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash
import json

#This is a text file with my db username and PW etc.
params = open('dbparams.txt').read()
#params = open('/home/ubuntu/Yahoo/dbparams.txt').read()
params =  params.split(',')


# create our little application :)
app = Flask(__name__)


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

	qDate = '2014-09-03'
	
	db = mysql.connect(user=params[0],password=params[1],host=params[2],database=params[3])
	cursor = db.cursor()

	cursor.execute('''SELECT qDate, tBucket, avg(tPrice),max(tPrice),min(tPrice) FROM livePrices WHERE Ticker=%s AND qDate=%s AND tPrice!='Null' GROUP BY tBucket ORDER BY qTime DESC LIMIT %s''',(tkr,qDate,n))

	outPut=[]
	for each in cursor:
		outPut.append([str(each[0]),str(each[1]),round(each[2],2),round(each[3],2),round(each[4],2)])

	dats = {'Ticker':tkr,'Prices':outPut}
	return json.dumps(dats,separators=(',', ':'))


@app.route('/keystats/<stkReq>')
def stock_stats(stkReq):
	return "YEAH BUDDY! "+stkReq


if __name__ == '__main__':
	port=int(os.environ.get('PORT', 5000))
	app.run(port=port)

