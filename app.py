# import the flask class
from flask import Flask, session, render_template, request,make_response,redirect,flash
# from flask_mysql import MySQL
from flaskext.mysql import MySQL

# instatiating flask class 
app=Flask(__name__)
mysql = MySQL()

# configuring MySQL for the web application
app.config['MYSQL_DATABASE_USER'] = 'root'    # default user of MySQL to be replaced with appropriate username
app.config['MYSQL_DATABASE_PASSWORD'] = '' # default passwrod of MySQL to be replaced with appropriate password
app.config['MYSQL_DATABASE_DB'] = 'pathology'  # Database name to be replaced with appropriate database name
app.config['MYSQL_DATABASE_HOST'] = 'localhost' # default database host of MySQL to be replaced with appropriate database host
#initialise mySQL
mysql.init_app(app)
#creating connection to access data
conn = mysql.connect()

@app.route('/')
def home():
    # return("HELLO!!")
    return render_template("home.html")