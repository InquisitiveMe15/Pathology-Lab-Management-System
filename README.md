# PATHOLOGY LAB MANAGEMENT SYSTEM

Project of CS257

Group G1

Members : Neha, Kanchi Pardhi, Khushi Verma, Shruti Modi (Roll Numbers - 200001051, 200001032, 200001036, 200001047 respectively)

## INTRODUCTION

Our web-based application serves as a fruitful database management system for Pathology Labs. It has role-based access, secure otp verification, login system with a user-friendly and interactive interface. 

It enables lab staff to add or edit patient, test, equipment, doctor details. They can choose tests for a given patient and place an order for him/her. Opon placing order, the system generates a bill and emails the receipt along with brochure to the patient's email. Patients can fill/ view their details using the app for faster operation which further eases the uses of the application.

Name and Logo of the Hypothtical Laboratory shown: G1 Pathology Lab 

<img width="90" alt="logo" src="https://user-images.githubusercontent.com/78869960/142638344-cb3b70fc-0a4f-4a7a-ad42-b99e9cce1446.png">


## LANGUAGES, TOOLS USED

We have used Python, Flask, MySQL, HTML, CSS, Javascript, Bootstrap frameworks for builiding our project mainly. The proper use of these tools have helped us heavily in developing the project efficiently.

## USING THE APPLICATION

The code files can be made to run locally on the system. One needs to download the .zip file of our codes from the github repo: https://github.com/InquisitiveMe15/Pathology-Lab-Management-System/ After extracting the files, one can navigate to the proper folders through the terminal.

* Thereafter, create a virtual environment locally using `python -m venv name` and actiavte it using `name/Scripts/activate`

* Following, run `pip install flask, flaskext.mysql, pdfkit` in the terminal and check for any other library that might be causing some difficulty on your system. 

* Next, one can run the 'sql_queries.sql' file on their MysqlWorkbench or any other installed database management tool. This will create the database schema on the system. 

* Along with this, go ahead and edit the 'app.py' file to fill in your user credetials like 'mysql_username', 'password', 'mail_id', 'mail_password', as required.

Once these steps are complete, go ahead and run `python app.py` This will run the application on localhost port. Navigate to the web page and explore the enjoyable Web Application.

# THE APPLICATION

Let us have a brief overview of the key features of the application. The following points highlight some interesting and useful aspects of the project app.

## LANDING PAGE <br />

We have make our project in such a way that it can be used both by the labstaff as well as the patients. <br />
Lab staff has a password through which they can enter the system. <br />

![Screenshot (516)](https://user-images.githubusercontent.com/85685489/142489836-e119abe6-8876-4388-a8d1-81c52f084a02.png) <br />

<img width="484" alt="Screenshot 2021-11-19 014549" src="https://user-images.githubusercontent.com/85685489/142490151-7e4e44e9-2062-41c5-ad12-fdd6033cdd47.png"> <br />

Already registered patients can view their profile and their test history using their login credentials i.e. their ID and their registered mail. <br />

<img width="482" alt="Screenshot 2021-11-19 014727" src="https://user-images.githubusercontent.com/85685489/142490363-c8072e28-4a3e-4bd7-aa38-7e63906e891e.png"> <br />

An example <br />

![Screenshot (517)](https://user-images.githubusercontent.com/85685489/142490634-9bd5180a-8399-4f62-9476-e00fb0e56723.png) <br />

Here at the profile page **logout** button is also given by clicking on which user will be redirected to the landing page again. <br />
On the landing page we have given the facility to make accounts of the new patients, they can do it themselves. <br />

<img width="467" alt="Screenshot 2021-11-19 015208" src="https://user-images.githubusercontent.com/85685489/142490978-169e87ff-9bed-40f1-b31e-c1a7bc85203f.png"> <br />

**Here, user ID will be pre-filled as user don't know whether a particular ID exists or not so he can use the one provided by the database itself.** <br />
It has all the verifying features like if the user submits a partially filled form then a warning will be shown and also the ID unique feature is also implemented. <br />

After successfully adding a patient a **green** colour alert will be there that the patient is added successfully and the ID will automatically increment by one. <br />

<img width="486" alt="Screenshot 2021-11-19 015536" src="https://user-images.githubusercontent.com/85685489/142491580-68161be6-f606-4f0f-b446-d73b788d251c.png"> <br />

That's all about the landing page. <br />

Now, we will login into the system using the password. <br />
Then we will land on to the Home page. <br />

## HOME PAGE

Here, we have various features like logout, add patient, test, doctor, equipments, place order, etc. <br />
At the bottom of the page contact details are given. <br />

![Screenshot (518)](https://user-images.githubusercontent.com/85685489/142491874-24a7b07e-eadb-49b8-875f-d06055775079.png) <br />
<img width="947" alt="Screenshot 2021-11-19 015840" src="https://user-images.githubusercontent.com/85685489/142491896-6604b54b-070c-4a02-8a73-3406b3adb423.png"> <br />

We have a search bar too for searching registered patients. <br />

**Example** <br />

![Screenshot (519)](https://user-images.githubusercontent.com/85685489/142492263-daa3a866-7932-48e6-81fd-e3129aa7c009.png) <br />
From here we can view the respective patient profile page and can also edit his/her details. <br />


## ADD, EDIT, VIEW PATIENTS

The application provides user-friendly interface to play around with the database in a secure manner. Viewing and Searching for existing patients by their name can be done by the Search Bar.

![Screenshot (961)](https://user-images.githubusercontent.com/78869960/142481810-724e387d-50b6-4a56-a03e-a15ffea14d82.png)

'Add Pateint' tab opens up a form before us to enter the new patient details. One of the entries of the form, namely, Patient ID comes auto-filled as it is managed by the database automatically to maintain integrity in the system. I f the user forgets to fill any of the required details, an error message notifying him is displayed.

![Screenshot (962)](https://user-images.githubusercontent.com/78869960/142482165-b2727b3f-a656-40ad-afb2-1de907861809.png)

Once some patient has been added successfully to the system, we can go ahead and Edit any of his details.


## ADD, EDIT, VIEW DOCTORS

Similar features go ahead for the 'Doctors' field, we can add new doctors to the database by filling up a form, edit the details of the existing doctors, and also view the list of all doctors associated with the lab, under the 'Doctors' tab.

![Screenshot (963)](https://user-images.githubusercontent.com/78869960/142482513-cc4d9c4d-1a2c-4ad3-a0bd-a69eb2f55665.png)

![Screenshot (964)](https://user-images.githubusercontent.com/78869960/142482782-98425ad0-c220-406b-9e94-59a51074b939.png)


## ADD, EDIT, VIEW TESTS

'Test' is another entity that we have used in our system, the receptionist can add new Tests to the database, along with their details like Test Name, Price, and also Edit them later if needed. Similarly, all the available tests can be seen in the form of a table under the 'View Tests' option. 
In all these cases, the unique feature of IDs is auto-maintatined by the system, without us having to worry about it. 

![Screenshot (965)](https://user-images.githubusercontent.com/78869960/142482890-b91f6311-b007-4cd1-b3cb-fff7f8a17076.png)

![Screenshot (966)](https://user-images.githubusercontent.com/78869960/142483014-0c8f7998-df22-40f8-96e1-239ebb142926.png)


## ADD, EDIT, VIEW, DELETE EQUIPMENTS

The user can likewise maintain the database of the available Equipments in the pathology lab. Adding, Editing Equipments can be done similar to the above entities, along with that any of the equipments can be Deleted from the database with the Delete option. We also maintain the STock Quantity of each equipment in the laboratory, and if the available quantity of any equipment is below 20, we show a warning for the same to be refilled.
![Screenshot (967)](https://user-images.githubusercontent.com/78869960/142483125-15445ba5-5576-4457-9c84-bccf24389a3a.png)

![Screenshot (968)](https://user-images.githubusercontent.com/78869960/142483498-e5860777-a719-4475-988b-05a2ff7606d5.png)

 So these cover up all the entities used in the system.


## PLACE ORDER

The order can be placed for the patient by filling all the required details in place order page.
.
![Screenshot (489)](https://user-images.githubusercontent.com/78892305/142486192-89969ba3-2f6c-44c6-ad3a-3be423aa965a.png)
![Screenshot (490)](https://user-images.githubusercontent.com/78892305/142486196-840fbaf7-a2ac-4aaa-a0f8-df77c0b97400.png)

Then we click on proceed to payment.

### OTP VERIFICATION

And the otp verification page opens up.

![Screenshot (491)](https://user-images.githubusercontent.com/78892305/142486199-13ec725a-83de-415f-98b1-bfbba5f5a1b0.png)

Then otp is sent to the patient.

![Screenshot (492)](https://user-images.githubusercontent.com/78892305/142486204-285bb658-2634-4fc6-8d6d-71a2284255a5.png)
![Screenshot (493)](https://user-images.githubusercontent.com/78892305/142486206-2cf0f1a6-0418-4184-b0bd-6db4ce61d005.png)
![Screenshot (494)](https://user-images.githubusercontent.com/78892305/142486209-71fd7ca7-3107-46f9-87a6-3853179bc141.png)

### MAILING THE BILL

After verifying otp the bill is mailed to the patient along with the pdf of pathalogy lab brouchre.

![Screenshot (496)](https://user-images.githubusercontent.com/78892305/142486210-e08d8769-ae51-4309-b2cc-e4b9ec711f4c.png)

![WhatsApp Image 2021-11-19 at 01 03 33](https://user-images.githubusercontent.com/78892305/142486437-3d2aa7c7-5dda-4727-92af-ff8e5310d5ad.jpeg)
![WhatsApp Image 2021-11-19 at 01 03 33 (1)](https://user-images.githubusercontent.com/78892305/142486446-98274039-cf02-4da7-9663-be063b70ca3e.jpeg)


## CONCLUDING

This sums up our project. We all teammates would like to thank our faculty, course teachers for providing us this wonderful opportunity to work on this enriching project. Working in this amazing team group has been a pleasnt journey full of new learnings each day. We built upon our tech and soft skills, with each phase of developing this project. Thank you very much.



