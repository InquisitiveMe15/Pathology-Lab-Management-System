from flask import Flask, session, render_template, request, make_response, redirect, flash, jsonify
# from flask_mysql import MySQL
from flaskext.mysql import MySQL
from datetime import date

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

@app.route('/')
def verification():
    return render_template("login.html", messg = 1)

@app.route('/login', methods = ['POST'])
def login():
    password = request.form['pwd']
    if password == 'project':
        return render_template("home.html")
    else:
        return render_template("login.html", messg = 0)

@app.route('/home')
def home():
    return render_template("home.html")


@app.route('/addPatientPage')
def addPatientPage():
    return render_template("addpatient.html")


@app.route('/addDoctorPage')
def addDoctorPage():
    return render_template("adddoctor.html")

@app.route('/editPatientPage/<string:patientId>/<string:name>/<string:gender>/<string:age>/<string:mobileNumber>/<string:email>/<string:address>')
def editPatientPage(patientId,name,gender,age,mobileNumber,email,address):
    return render_template('editpatient.html', patientId = patientId, name = name, gender = gender, age = age, mobileNumber = mobileNumber, email = email, address = address)
    return("Working")

@app.route('/editDoctorPage/<string:doctorName>/<string:doctorId>/<string:email>/<string:mobileNumber>')
def editDoctorPage(doctorName,doctorId,email,mobileNumber):
    return render_template("editdoctor.html", doctorName = doctorName, doctorId = doctorId, email = email, mobileNumber = mobileNumber)


@app.route('/addTestPage')
def addTestPage():
    return render_template("addtest.html")


@app.route('/editTestPage/<string:testId>/<string:testName>/<string:price>')
def editTestPage(testId,testName,price):
    return render_template("editTest.html", testId = testId, testName = testName, price = price)


@app.route('/addEquipmentPage')
def addEquipmentPage():
    return render_template("addequipment.html")


@app.route('/editEquipmentPage/<string:equipmentId>/<string:equipmentName>/<string:price>/<string:instock>')
def editEquipmentPage(equipmentId,equipmentName,price,instock):
    return render_template("editequipment.html", equipmentId = equipmentId, equipmentName = equipmentName, price = price, instock = instock)





cursor.execute('SELECT * FROM test')
testlist = cursor.fetchall()
cursor.execute('SELECT name FROM patient')
patientnamelist = cursor.fetchall()
cursor.execute('SELECT patientId FROM patient')
patientidlist = cursor.fetchall()
cursor.execute('SELECT name FROM doctor')
doctornamelist = cursor.fetchall()
cursor.execute('SELECT id FROM doctor')
doctoridlist = cursor.fetchall()




@app.route('/placeOrderPage')
def placeOrderPage():
    # cursor.execute('SELECT * FROM test')
    # testlist = cursor.fetchall()
    # # print(testlist)
    # cursor.execute('SELECT name FROM patient')
    # patientnamelist = cursor.fetchall()
    # cursor.execute('SELECT patientId FROM patient')
    # patientidlist = cursor.fetchall()
    # cursor.execute('SELECT name FROM doctor')
    # doctornamelist = cursor.fetchall()
    cursor.execute('SELECT orderId FROM order1')
    orderlist=cursor.fetchall()
    totalorder=cursor.rowcount
    totalorder=totalorder+1
    return render_template("placeorder.html", testlist=testlist, patientnamelist=patientnamelist, patientidlist=patientidlist, doctornamelist = doctornamelist,totalorder=totalorder,doctoridlist=doctoridlist)
    return("Working")


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


@app.route('/AddDoctor', methods=['GET', 'POST'])
def AddDoctor():
    warning = ''
    if request.method == 'POST' and 'doctorName' in request.form and 'doctorId' in request.form and 'email' in request.form and 'mobileNumber' in request.form:
        # print("YES")
        doctorName = request.form['doctorName']
        doctorId = request.form['doctorId']
        email = request.form['email']
        mobileNumber = request.form['mobileNumber']
        cursor.execute(
            'SELECT * FROM doctor WHERE Id = % s', (doctorId,))
        doctor = cursor.fetchone()
        if doctor:
            warning = "This Doctor Id already exists."
        elif not doctorId or not doctorName or not email or not mobileNumber:
            warning = 'Please fill all the required details first !'
        else:
            cursor.execute('INSERT INTO doctor VALUES (%s, % s, % s, % s)',
                           (doctorId, doctorName, email, mobileNumber))
            conn.commit()
            warning = 'Doctor added successfully ! '
    return render_template('adddoctor.html', warning=warning)


@app.route('/AddEquipment', methods=['GET', 'POST'])
def AddEquipment():
    warning = ''
    if request.method == 'POST' and 'equipmentName' in request.form and 'equipmentId' in request.form and 'price' in request.form and 'instock' in request.form:
        # print("YES")
        equipmentName = request.form['equipmentName']
        equipmentId = request.form['equipmentId']
        price = request.form['price']
        instock = request.form['instock']
        cursor.execute(
            'SELECT * FROM equipments WHERE id = % s', (equipmentId,))
        equipment = cursor.fetchone()
        if equipment:
            warning = "This Equipment Id already exists."
        elif not equipmentId or not equipmentName or not price or not instock:
            warning = 'Please fill all the required details first !'
        else:
            cursor.execute('INSERT INTO equipments VALUES (%s, % s, % s, % s)',
                           (equipmentId, equipmentName, price, instock))
            conn.commit()
            warning = 'Equipment added successfully ! '
    return render_template('addequipment.html', warning=warning)


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


@app.route('/DoctorPage')
def DoctorPage():
    doctorId = []
    doctorName = []
    email = []
    mobileNumber = []
    query_string = ("SELECT Id FROM doctor")
    cursor.execute(query_string)
    row = cursor.fetchone()
    while(row != None):
        doctorId.append(row[0])
        row = cursor.fetchone()
    print(doctorId)

    for id in doctorId:
        query_string = (
            "SELECT name FROM doctor WHERE Id='{}'".format(id))
        cursor.execute(query_string)
        row = cursor.fetchone()
        while(row != None):
            doctorName.append(row[0])
            row = cursor.fetchone()
    print(doctorName)

    for id in doctorId:
        query_string = (
            "SELECT email FROM doctor WHERE Id='{}'".format(id))
        cursor.execute(query_string)
        row = cursor.fetchone()
        while(row != None):
            email.append(row[0])
            row = cursor.fetchone()
    print(email)

    for id in doctorId:
        query_string = (
            "SELECT mobile_number FROM doctor WHERE Id='{}'".format(id))
        cursor.execute(query_string)
        row = cursor.fetchone()
        while(row != None):
            mobileNumber.append(row[0])
            row = cursor.fetchone()
    print(mobileNumber)

    result = []
    length = len(doctorId)
    result.append(doctorId)
    result.append(doctorName)
    result.append(email)
    result.append(mobileNumber)
    return render_template("doctor.html", result=result, length=length)
    return("working")


@app.route('/equipmentPage')
def equipmentPage():
    equipmentId = []
    equipmentName = []
    price = []
    instock = []
    query_string = ("SELECT id FROM equipments")
    cursor.execute(query_string)
    row = cursor.fetchone()
    while(row != None):
        equipmentId.append(row[0])
        row = cursor.fetchone()
    print(equipmentId)

    for id in equipmentId:
        query_string = (
            "SELECT name FROM equipments WHERE id='{}'".format(id))
        cursor.execute(query_string)
        row = cursor.fetchone()
        while(row != None):
            equipmentName.append(row[0])
            row = cursor.fetchone()
    print(equipmentName)

    for id in equipmentId:
        query_string = (
            "SELECT price FROM equipments WHERE id='{}'".format(id))
        cursor.execute(query_string)
        row = cursor.fetchone()
        while(row != None):
            price.append(row[0])
            row = cursor.fetchone()
    print(price)

    for id in equipmentId:
        query_string = (
            "SELECT in_stock FROM equipments WHERE id='{}'".format(id))
        cursor.execute(query_string)
        row = cursor.fetchone()
        while(row != None):
            instock.append(row[0])
            row = cursor.fetchone()
    print(instock)

    result = []
    length = len(equipmentId)
    result.append(equipmentId)
    result.append(equipmentName)
    result.append(price)
    result.append(instock)

    #if any equipment has its left quantity less than 20 then a warning will be shown
    alert_names=[]
    index=0
    for number in instock:
        if number < 20:
            alert_names.append(equipmentName[index])
        index=index+1
    if len(alert_names)!=0:
        return render_template("equipment.html", result=result, length=length, alert_names = alert_names)

    return render_template("equipment.html", result=result, length=length)
    return("working")


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
        search_word = request.form['query']
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


@app.route('/EditDoctor', methods=["POST", "GET"])
def EditDoctor():
    warning = ''
    if request.method == 'POST' and 'doctorId' in request.form and 'doctorName' in request.form and 'email' in request.form and 'mobileNumber' in request.form:
        doctorId = request.form['doctorId']
        doctorName = request.form['doctorName']
        email = request.form['email']
        mobileNumber = request.form['mobileNumber']
        cursor.execute(
            'SELECT * FROM doctor WHERE Id = % s', (doctorId,))
        doctor = cursor.fetchone()
        if doctor == None:
            warning = "Doctor ID doesn't exists"
        elif not doctorId or not doctorName or not email or not mobileNumber:
            warning = 'Please fill all the required details first !'
        else:
            query_string = "UPDATE doctor SET name='{}', email='{}', mobile_number='{}' WHERE Id='{}'".format(
                doctorName, email, mobileNumber, doctorId)
            cursor.execute(query_string)
            conn.commit()
            warning = 'Doctor details updated.'
    return render_template('editdoctor.html', warning=warning)
    return("Working")

@app.route('/EditPatient', methods=["POST", "GET"])
def EditPatient():
    warning = ''
    if request.method == 'POST' and 'patientId' in request.form and 'name' in request.form and 'gender' in request.form and 'age' in request.form and 'address' in request.form and 'mobileNumber' in request.form and 'email' in request.form:
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
        if patient == None:
            warning = "Patient ID doesn't exists"
        elif not patientId or not name or not gender or not age or not address or not mobileNumber or not email:
            warning = 'Please fill all the required details first !'
        else:
            query_string = "UPDATE patient SET name='{}', gender='{}', age='{}', mobileNumber='{}', email='{}', address='{}' WHERE patientId='{}'".format(
                name, gender, age, mobileNumber, email, address, patientId)
            cursor.execute(query_string)
            conn.commit()
            warning = 'Patient details updated.'
    return render_template('editpatient.html', warning=warning)
    return("Working")


@app.route('/EditEquipment', methods=["POST", "GET"])
def EditEquipment():
    warning = ''
    if request.method == 'POST' and 'equipmentId' in request.form and 'equipmentName' in request.form and 'price' in request.form and 'instock' in request.form:
        equipmentId = request.form['equipmentId']
        equipmentName = request.form['equipmentName']
        price = request.form['price']
        instock = request.form['instock']
        cursor.execute(
            'SELECT * FROM equipments WHERE id = % s', (equipmentId,))
        equipment = cursor.fetchone()
        if equipment == None:
            warning = "Equipment ID doesn't exists"
        elif not equipmentId or not equipmentName or not price or not instock:
            warning = 'Please fill all the required details first !'
        else:
            query_string = "UPDATE equipments SET name='{}', price='{}', in_stock='{}' WHERE id='{}'".format(
                equipmentName, price, instock, equipmentId)
            cursor.execute(query_string)
            conn.commit()
            warning = 'Equipment details updated.'
    return render_template('editequipment.html', warning=warning)
    return("Working")


@app.route('/makebill', methods=['GET', 'POST'])
def makebill():
    if request.method == 'POST' and 'patientname' in request.form and 'patientId' in request.form and 'doctorname' in request.form and 'test1' in request.form and 'test2' in request.form and 'test3' in request.form and 'test4' in request.form:
        warning = ''
        orderId=request.form['orderId']
        patientname = request.form['patientname']
        patientId = request.form['patientId']
        doctorId = request.form['doctorId']
        doctorname = request.form['doctorname']
        alltest = []
        test1 = request.form['test1']
        if(test1 != "NULL"):
            alltest.append(test1)
        test2 = request.form['test2']
        if(test2 != "NULL"):
            alltest.append(test2)
        test3 = request.form['test3']
        if(test3 != "NULL"):
            alltest.append(test3)
        test4 = request.form['test4']
        if(test4 != "NULL"):
            alltest.append(test4)
        query_string = "SELECT name FROM patient WHERE patientId='{}'".format(patientId)
        cursor.execute(query_string)
        real_name = cursor.fetchone()
        # print(real_name[0])
        
        if patientname == 'NULL' or patientId == 'NULL' or doctorname == 'NULL'or doctorId=='NULL':
            warning = 'Please fill all the required details first !'
        
        elif real_name[0] != patientname:
            warning = "Name and Id doesn't match with the registered values. Fill correct details."
        elif len(alltest)==0:
            warning = 'Please select atleast one test.'
        else:
            email = []
            query_string = (
                "SELECT email FROM patient WHERE patientId='{}'".format(patientId))
            cursor.execute(query_string)
            row = cursor.fetchone()
            email.append(row[0])
            patientemail = email[0]

            alltestid = []
            for name in alltest:
                query_string = (
                    "SELECT testId FROM test WHERE testName='{}'".format(name))
                cursor.execute(query_string)
                row = cursor.fetchone()
                while(row != None):
                    alltestid.append(row[0])
                    row = cursor.fetchone()
            print(alltestid)
            

            alltestprice = []
            for name in alltest:
                query_string = "SELECT price FROM test WHERE testName='{}'".format(name)
                cursor.execute(query_string)
                row = cursor.fetchone()
                while(row != None):
                    alltestprice.append(row[0])
                    row = cursor.fetchone()
            print(alltestprice)

            result = []
            length = len(alltest)
            total = sum(int(alltestprice[i]) for i in range(length))
            result.append(alltestid)
            result.append(alltest)
            result.append(alltestprice)
            date1=date.today()
        
            cursor.execute('INSERT INTO order1 VALUES (%s,%s,%s,%s)',(orderId,date1,total,doctorId))
            conn.commit()
            cursor.execute('INSERT INTO givesorder VALUES (%s,%s)',(orderId,patientId))
            conn.commit()
            for i in range(len(alltestid)):
                tID=alltestid[i]
                cursor.execute('INSERT INTO contains VALUES (%s,%s)',(orderId,tID))
                conn.commit()
            return render_template("bill.html", result=result, length=length, total=total, patientname=patientname, patientemail=patientemail, doctorname = doctorname)
        return render_template("placeorder.html", warning = warning, testlist=testlist, patientnamelist=patientnamelist, patientidlist=patientidlist, doctornamelist = doctornamelist)
    return("Error.")


@app.route('/deleteEquipment/<string:equipmentId>')
def deleteEquipment(equipmentId):
    query_string = "DELETE FROM equipments WHERE id='{}'".format(equipmentId)
    cursor.execute(query_string)
    conn.commit()
    return redirect(('/equipmentPage'))


@app.route('/deleteTest/<string:testId>')
def deleteTest(testId):
    query_string = "DELETE FROM test WHERE testId='{}'".format(testId)
    cursor.execute(query_string)
    conn.commit()
    return redirect(('/viewTestPage'))


@app.route('/deleteDoctor/<string:doctorId>')
def deleteDoctor(doctorId):
    query_string = "DELETE FROM doctor WHERE id='{}'".format(doctorId)
    cursor.execute(query_string)
    conn.commit()
    return redirect(('/DoctorPage'))


@app.route('/about')
def about():
    return render_template("about.html")

if __name__ == '__main__':
    app.run(debug=True)