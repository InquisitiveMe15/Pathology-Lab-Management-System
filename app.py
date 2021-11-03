from flask import Flask, session, render_template, request, make_response, redirect, flash, jsonify
# from flask_mysql import MySQL
from flaskext.mysql import MySQL


app = Flask(__name__)
mysql = MySQL()

# configuring MySQL for the web application
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'kanchi123456@'
app.config['MYSQL_DATABASE_DB'] = 'pathology'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)
conn = mysql.connect()
cursor = conn.cursor()

cursor.execute('SELECT * FROM test')
testlist = cursor.fetchall()
cursor.execute('SELECT name FROM patient')
patientnamelist = cursor.fetchall()
cursor.execute('SELECT name FROM doctor')
doctornamelist = cursor.fetchall()
@app.route('/')
def home():
    return render_template("home.html")


@app.route('/addPatientPage')
def addPatientPage():
    return render_template("addpatient.html")

# @app.route('/viewTestPage')
# def viewTestPage():
#     return("Working")
#     return render_template("viewtest.html")


@app.route('/addTestPage')
def addTestPage():
    return render_template("addtest.html")

@app.route('/editTestPage')
def editTestPage():
    return render_template("editTest.html")


@app.route('/placeOrderPage')
def placeOrderPage():
    print(testlist)
    return render_template("placeorder.html", testlist=testlist,patientnamelist=patientnamelist,doctornamelist=doctornamelist)
    return("Working")
@app.route('/makebill', methods=['GET', 'POST'])
def makebill():
    if request.method == 'POST':
        patientname = request.form['patientname']
        doctorname = request.form['doctorname']
        alltest=[]
        test1= request.form['test1']
        if(test1 !="NULL"):
            alltest.append(test1)
        test2=request.form['test2']
        if(test2 !="NULL"):
            alltest.append(test2) 
        test3=request.form['test3']
        if(test3 !="NULL"):
            alltest.append(test3)
        test4=request.form['test4']
        if(test4 !="NULL"):
            alltest.append(test4)
        print(test1)  
        print(test2)
        
    alltestid=[]
    for name in alltest:
        query_string = ("SELECT testId FROM test WHERE testName='{}'".format(name))
        cursor.execute(query_string)
        row = cursor.fetchone()
        while(row != None):
            alltestid.append(row[0])
            row = cursor.fetchone()
    print(alltestid)

    alltestprice=[]
    for name in alltest:
        query_string = ("SELECT price FROM test WHERE testName='{}'".format(name))
        cursor.execute(query_string)
        row = cursor.fetchone()
        while(row != None):
            alltestprice.append(row[0])
            row = cursor.fetchone()
    print(alltestprice)
     
    result = []
    length = len(alltest)
    total=sum(int(alltestprice[i]) for i in range(length))
    result.append(alltestid)
    result.append(alltest)
    result.append(alltestprice)
    return render_template("bill.html", result=result, length=length,total=total,patientname=patientname,doctorname=doctorname)
    return("working")


        



@app.route('/AddPatient', methods=['GET', 'POST'])
def AddPatient():
    warning = ''
    if request.method == 'POST' and 'patientId' in request.form and 'name' in request.form and 'gender' in request.form and 'age' in request.form and 'address' in request.form and 'mobileNumber' in request.form and 'email' in request.form:
        # print("YES")
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
            warning = "This patientId already exists."
        elif not patientId or not name or not gender or not age or not address or not mobileNumber or not email:
            warning = 'Please fill all the required details first !'
        else:
            cursor.execute('INSERT INTO patient VALUES (%s, % s, % s, % s, %s, %s, %s)',
                           (patientId, name, gender, age, mobileNumber, email, address))
            conn.commit()
            warning = 'Patient added successfully ! '
    return render_template('addpatient.html', warning=warning)


@app.route('/AddTest', methods=['GET', 'POST'])
def AddTest():
    warning = ''
    if request.method == 'POST' and 'testId' in request.form and 'testName' in request.form and 'price' in request.form:
        # print("YES")
        testId = request.form['testId']
        testName = request.form['testName']
        price = request.form['price']

        cursor.execute(
            'SELECT * FROM test WHERE testId = % s', (testId,))
        test = cursor.fetchone()
        if test:
            warning = "This testId already exists."
        elif not testId or not testName or not price:
            warning = 'Please fill all the required details first !'
        else:
            cursor.execute('INSERT INTO test VALUES (%s, % s, % s)',
                           (testId, testName, price))
            conn.commit()
            warning = 'Test added successfully ! '
    return render_template('addtest.html', warning=warning)


@app.route('/viewTestPage')
def viewTestPage():
    testId = []
    testName = []
    price = []
    query_string = ("SELECT testId FROM test")
    cursor.execute(query_string)
    row = cursor.fetchone()
    while(row != None):
        testId.append(row[0])
        row = cursor.fetchone()
    print(testId)

    for id in testId:
        query_string = (
            "SELECT testName FROM test WHERE testId='{}'".format(id))
        cursor.execute(query_string)
        row = cursor.fetchone()
        while(row != None):
            testName.append(row[0])
            row = cursor.fetchone()
    print(testName)

    query_string = ("SELECT price FROM test")
    cursor.execute(query_string)
    row = cursor.fetchone()
    while(row != None):
        price.append(row[0])
        row = cursor.fetchone()
    print(price)

    result = []
    length = len(testId)
    result.append(testId)
    result.append(testName)
    result.append(price)
    return render_template("viewTest.html", result=result, length=length)
    return("working")


@app.route("/ajaxlivesearch", methods=["POST", "GET"])
def ajaxlivesearch():
    # cursor = conn.cursor(MySQLdb.cursors.DictCursor)
    if request.method == 'POST':
        search_word = request.form['sendData']
        # print(search_word)
        if search_word == '':
            query = "SELECT * from patient ORDER BY patientId"
            cursor.execute(query)
            numrows = int(cursor.rowcount)
            patient = cursor.fetchall()
        else:
            query = "SELECT * from patient WHERE name LIKE '%{}%'  ORDER BY patientId DESC LIMIT 20".format(
                search_word)
            cursor.execute(query)
            numrows = int(cursor.rowcount)
            patient = cursor.fetchall()

    return jsonify({'htmlresponse': render_template('response.html', patient=patient, numrows=numrows)})

@app.route('/EditTest', methods=["POST", "GET"])
def EditTest():
    warning = ''
    if request.method == 'POST' and 'testId' in request.form and 'testName' in request.form and 'price' in request.form:
        testId = request.form['testId']
        testName = request.form['testName']
        price = request.form['price']
        cursor.execute(
            'SELECT * FROM test WHERE testId = % s', (testId,))
        test = cursor.fetchone()
        if test == None:
            warning = "Test ID doesn't exists"
        elif not testId or not testName or not price:
            warning = 'Please fill all the required details first !'
        else:
            query_string = "UPDATE test SET testName='{}', price='{}' WHERE testId='{}'".format(
                testName, price, testId)
            cursor.execute(query_string)
            conn.commit()
            warning = 'Test details updated.'
    return render_template('editTest.html', warning=warning)
    return("Working")

if __name__ == '__main__':
    app.run(debug=True)