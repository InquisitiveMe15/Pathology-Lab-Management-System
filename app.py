from flask import Flask, session, render_template, request,make_response,redirect,flash,jsonify
# from flask_mysql import MySQL
from flaskext.mysql import MySQL


app=Flask(__name__)
mysql = MySQL()

# configuring MySQL for the web application
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'Thds@19xcNh#20J' 
app.config['MYSQL_DATABASE_DB'] = 'pathology'
app.config['MYSQL_DATABASE_HOST'] = 'localhost' 
mysql.init_app(app)
conn = mysql.connect()
cursor = conn.cursor()


@app.route('/')
def home():
    return render_template("home.html")

@app.route('/addPatientPage')
def addPatientPage():
    return render_template("addpatient.html")

@app.route('/AddPatient', methods=['GET', 'POST'])
def AddPatient():
    warning = ''
    if request.method == 'POST' and 'patientId' in request.form and 'name' in request.form and 'gender' in request.form and 'age' in request.form and 'address' in request.form and 'mobileNumber' in request.form and 'email' in request.form:
        print("YES")
        patientId = request.form['patientId']
        name = request.form['name']
        gender = request.form['gender']
        age = request.form['age']
        address = request.form['address']
        mobileNumber = request.form['mobileNumber']
        email = request.form['email']
        cursor.execute(
            'SELECT * FROM patient WHERE patientId = % s', (patientId,))
        patient = cursor.fetchone()
        if patient:
            warning = "This patient patientId already exists."
        elif not patientId or not name or not gender or not age or not address or not mobileNumber or not email:
            warning = 'Please fill all the required details first !'
        else:
            cursor.execute('INSERT INTO patient VALUES (%s, % s, % s, % s, %s, %s, %s)',
                           (patientId, name, gender, age, mobileNumber, email, address))
            conn.commit()
            warning = 'Patient added successfully ! '
    return render_template('addpatient.html', warning=warning)

@app.route("/ajaxlivesearch",methods=["POST","GET"])
def ajaxlivesearch():
    # cursor = conn.cursor(MySQLdb.cursors.DictCursor)
    if request.method == 'POST':
        search_word = request.form['query']
        # print(search_word)
        if search_word == '':
            query = "SELECT * from patient ORDER BY patientId"
            cursor.execute(query)
            numrows = int(cursor.rowcount)
            patient = cursor.fetchall()
        else:    
            query = "SELECT * from patient WHERE name LIKE '%{}%'  ORDER BY patientId DESC LIMIT 20".format(search_word)
            cursor.execute(query)
            numrows = int(cursor.rowcount)
            patient = cursor.fetchall()
			
    return jsonify({'htmlresponse': render_template('response.html', patient=patient, numrows=numrows)})
