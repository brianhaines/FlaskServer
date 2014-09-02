import os
from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash


# create our little application :)
app = Flask(__name__)



@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/XOM')
def hello_world():
    return 'EXXON World!'

if __name__ == '__main__':
	port=int(os.environ.get('PORT', 5000))
	app.run(port=port)



# app.config.update(dict(
# 	DATABASE = os.path.join(app.root_path, 'flaskr.db'),
# 	DEBUG = True,
# 	SECRET_KEY = 'development key',
# 	USERNAME = 'admin',
# 	PASSWORD = 'default'
# ))
# app.config.from_envvar('FLASKR_SETTINGS', silent=True)