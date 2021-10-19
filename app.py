# import the flask class
# from flask import Flask, session, render_template, request,make_response,redirect,jsonify
# # from flask_mysql import MySQL
# from flaskext.mysql import MySQL

# # instatiating flask class
# app=Flask(__name__)
# mysql = MySQL()

# # configuring MySQL for the web application
# app.config['MYSQL_DATABASE_USER'] = 'root'    # default user of MySQL to be replaced with appropriate username
# app.config['MYSQL_DATABASE_PASSWORD'] = 'kanchi123456@' # default passwrod of MySQL to be replaced with appropriate password
# app.config['MYSQL_DATABASE_DB'] = 'pathology'  # Database name to be replaced with appropriate database name
# app.config['MYSQL_DATABASE_HOST'] = 'localhost' # default database host of MySQL to be replaced with appropriate database host
# #initialise mySQL
# mysql.init_app(app)
# #creating connection to access data
# conn = mysql.connect()
from flask import Flask, render_template, request, jsonify
from flask_mysqldb import MySQL,MySQLdb 
 
app = Flask(__name__)
        
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'kanchi123456@'
app.config['MYSQL_DB'] = 'pathology'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
mysql = MySQL(app)
@app.route('/')
def home():
    # return("HELLO!!")
    return render_template("home.html")
@app.route("/ajaxlivesearch",methods=["POST","GET"])
def ajaxlivesearch():
    cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    if request.method == 'POST':
        search_word = request.form['query']
        print(search_word)
        if search_word == '':
            query = "SELECT * from patient ORDER BY patientId"
            cur.execute(query)
            patient = cur.fetchall()
        else:    
            query = "SELECT * from patient WHERE name LIKE '%{}%'  ORDER BY patientId DESC LIMIT 20".format(search_word)
            cur.execute(query)
            numrows = int(cur.rowcount)
            patient = cur.fetchall()
			
    return jsonify({'htmlresponse': render_template('response.html', patient=patient, numrows=numrows)})



if __name__ == '__main__':
    app.run(debug=True)
