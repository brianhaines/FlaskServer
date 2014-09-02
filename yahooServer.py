#!/usr/bin/env python3
import os
import mysql.connector as mysql
from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash

#This is a text file with my db username and PW etc.
params = open('dbparams.txt').read()
#params = open('/home/ubuntu/Yahoo/dbparams.txt').read()
params =  params.split(',')


# create our little application :)
app = Flask(__name__)



@app.route('/')
def hello_world():
	return 'Hello World!'

@app.route('/<ticker>')
def stock_tip(ticker):
	# Hot stock tip here:
	tkr = ticker
	db = mysql.connect(user=params[0],password=params[1],host=params[2],database=params[3])
	cursor = db.cursor()

	cursor.execute('''SELECT tBucket, avg(tPrice) FROM livePrices WHERE Ticker=%s AND qDate='2014-09-02' AND tPrice!='Null' GROUP BY tBucket ORDER BY qTime DESC LIMIT 1''',(tkr,))

	for each in cursor:
		outPut = [str(each[0]),each[1]]
	
	return '%s is %s at %s' % (tkr,outPut[1],outPut[0])


if __name__ == '__main__':
	port=int(os.environ.get('PORT', 5000))
	app.run(port=port)

