Flask Price Server
===========

This Python project utilizes the Flask package to serve prices that I have stored in my AWS/RDS MySQL database. The intent is to host this app on Heroku and return data using JSON.

##Why I did this

The motivation for this project is to provide myself with an easy-to-use source of fine-grained price information. Returning the data in JSON will allow for easy and efficient access by future projects. This repo can be cloned to Heroku or it can be run locally.

##How to use it

Clone this repo locally and then push it to your Heroku. Be sure to edit Heroku's Environment Variables(`$ heroku config:set <EnvVar>=<value>` to allow access to your own MySQL database, wherever that may reside.

Heroku will shut down your app if it is not run for 20 minutes, so the response time of the first call to the app may be several seconds, otherwise it is very quick to respond.

Running locally is possible with the addition of a `.env` file with the Environment Variables set to your values.

This requires installation of the `Flask`, `gunicorn` and `mysql-connector-python` packages when run locally. Heroku will install all neccessary packages which are listed in the `requirements.txt` file.

##The Future

The next version of this app will be able to return the fundamental data which my database also contains. For now it will only return prices which is all I need from it for now. 

