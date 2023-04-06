from django.shortcuts import render
from django.template import RequestContext
from django.contrib import messages
import pymysql
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage
import os
from datetime import date
import os
import datetime

global userid,  slot, slotdate, doctorname, aid

def BookAppointment(request):
    if request.method == 'GET':
       return render(request, 'BookAppointment.html', {})

def index(request):
    if request.method == 'GET':
       return render(request, 'index.html', {})

def PatientLogin(request):
    if request.method == 'GET':
       return render(request, 'PatientLogin.html', {})    

def DoctorLogin(request):
    if request.method == 'GET':
       return render(request, 'DoctorLogin.html', {})

def PatientSignup(request):
    if request.method == 'GET':
        return render(request, 'PatientSignup.html', {})
        

def AddDoctor(request):
    if request.method == 'GET':
       return render(request, 'AddDoctor.html', {})

def AdminLogin(request):
    if request.method == 'GET':
       return render(request, 'AdminLogin.html', {})

def AdminLoginAction(request):
    if request.method == 'POST':
        global userid
        user = request.POST.get('t1', False)
        password = request.POST.get('t2', False)
        if user == "admin" and password == "admin":
            context= {'data':'Welcome '+user}
            return render(request, 'AdminScreen.html', context)
        else:
            context= {'data':'Invalid Login'}
            return render(request, 'AdminLogin.html', context)

def PatientSignupAction(request):
    if request.method == 'POST':
        username = request.POST.get('t1', False)
        password = request.POST.get('t2', False)
        email = request.POST.get('t3', False)
        contact = request.POST.get('t4', False)
        address = request.POST.get('t5', False)
        output = 'none'
        con = pymysql.connect(host='127.0.0.1',port = 3306,user = 'root', password = '', database = 'PatientApp',charset='utf8')
        with con:
            cur = con.cursor()
            cur.execute("select username FROM patientsignup")
            rows = cur.fetchall()
            for row in rows:
                if row[0] == username:
                    output = username+" Username already exists"                    
        if output == "none":
            db_connection = pymysql.connect(host='127.0.0.1',port = 3306,user = 'root', password = '', database = 'PatientApp',charset='utf8')
            db_cursor = db_connection.cursor()
            student_sql_query = "INSERT INTO patientsignup(username,password,contact_no,email,address) VALUES('"+username+"','"+password+"','"+contact+"','"+email+"','"+address+"')"
            db_cursor.execute(student_sql_query)
            db_connection.commit()
            print(db_cursor.rowcount, "Record Inserted")
            if db_cursor.rowcount == 1:
                context= {'data':'Signup process completed'}
                return render(request, 'PatientSignup.html', context)
            else:
                context= {'data':'Error in saving signup details'}
                return render(request, 'PatientSignup.html', context)
        else:
            context= {'data':output}
            return render(request, 'PatientSignup.html', context)  



def PatientLoginAction(request):
    if request.method == 'POST':
        global userid
        username = request.POST.get('t1', False)
        password = request.POST.get('t2', False)
        status = 'none'
        con = pymysql.connect(host='127.0.0.1',port = 3306,user = 'root', password = '', database = 'PatientApp',charset='utf8')
        with con:
            cur = con.cursor()
            cur.execute("select username,password FROM patientsignup")
            rows = cur.fetchall()
            for row in rows:
                if row[0] == username and row[1] == password:
                    userid = username
                    status = 'success'
                    break
        if status == 'success':
            output = 'Welcome '+username
            context= {'data':output}
            return render(request, 'PatientScreen.html', context)
        else:
            context= {'data':'Invalid username'}
            return render(request, 'PatientLogin.html', context)
        

def AddDoctorAction(request):
    if request.method == 'POST':
        username = request.POST.get('t1', False)
        password = request.POST.get('t2', False)
        email = request.POST.get('t3', False)
        contact = request.POST.get('t4', False)
        qualification = request.POST.get('t5', False)
        experience = request.POST.get('t6', False)
        hospital = request.POST.get('t7', False)
        address = request.POST.get('t8', False)
        speciality = request.POST.get('t9', False)
        output = 'none'
        con = pymysql.connect(host='127.0.0.1',port = 3306,user = 'root', password = '', database = 'PatientApp',charset='utf8')
        with con:
            cur = con.cursor()
            cur.execute("select username FROM adddoctor")
            rows = cur.fetchall()
            for row in rows:
                if row[0] == username:
                    output = username+" Username already exists"                    
        if output == "none":
            db_connection = pymysql.connect(host='127.0.0.1',port = 3306,user = 'root', password = '', database = 'PatientApp',charset='utf8')
            db_cursor = db_connection.cursor()
            student_sql_query = "INSERT INTO adddoctor(username,password,emailid,contact_no,qualification,experience_details,hospital_name,address,speciality) VALUES('"+username+"','"+password+"','"+email+"','"+contact+"','"+qualification+"','"+experience+"','"+hospital+"','"+address+"','"+speciality+"')"
            db_cursor.execute(student_sql_query)
            db_connection.commit()
            print(db_cursor.rowcount, "Record Inserted")
            if db_cursor.rowcount == 1:
                context= {'data':'Doctor details added'}
                return render(request, 'AddDoctor.html', context)
            else:
                context= {'data':'Error in adding doctor details'}
                return render(request, 'AddDoctor.html', context)
        else:
            context= {'data':output}
            return render(request, 'AddDoctor.html', context)  


def DoctorLoginAction(request):
    if request.method == 'POST':
        global userid, hospital
        username = request.POST.get('t1', False)
        password = request.POST.get('t2', False)
        status = 'none'
        con = pymysql.connect(host='127.0.0.1',port = 3306,user = 'root', password = '', database = 'PatientApp',charset='utf8')
        with con:
            cur = con.cursor()
            cur.execute("select username,password FROM adddoctor")
            rows = cur.fetchall()
            for row in rows:
                if row[0] == username and row[1] == password:
                    userid = username
                    status = 'success'
                    break
        if status == 'success':
            output = 'Welcome '+username
            context= {'data':output}
            return render(request, 'DoctorScreen.html', context)
        else:
            context= {'data':'Invalid username'}
            return render(request, 'DoctorLogin.html', context)


def ViewAdminDoctor(request):
    if request.method == 'GET':
        output = '<h4><b>View Doctor Details Screen</b></h4><table border="1" align="center" width="100%" ><tr>'
        font = '<font size="" color="black">'
        columns = ['Username','Password','Email ID','Contact No','Qualification', 'Experience Details', 'Hospital Name', 'Address', 'Speciality']
        for i in range(len(columns)):
            output += '<th>'+font+columns[i]+'</th>'
        output += "</tr>"    
        con = pymysql.connect(host='127.0.0.1',port = 3306,user = 'root', password = '', database = 'PatientApp',charset='utf8')
        with con:
            cur = con.cursor()
            cur.execute("select * FROM adddoctor")
            rows = cur.fetchall()
            for row in rows:
                output+='<tr><td>'+font+str(row[0])+'</td>'
                output+='<td>'+font+str(row[1])+'</td>'
                output+='<td>'+font+str(row[2])+'</td>'
                output+='<td>'+font+str(row[3])+'</td>'
                output+='<td>'+font+str(row[4])+'</td>'
                output+='<td>'+font+str(row[5])+'</td>'
                output+='<td>'+font+str(row[6])+'</td>'
                output+='<td>'+font+str(row[7])+'</td>'
                output+='<td>'+font+str(row[8])+'</td>'
        context= {'data':output}
        return render(request, 'ViewAdminReports.html', context)

def checkSlot(username, slot, choosen_date):
    count = 0
    con = pymysql.connect(host='127.0.0.1',port = 3306,user = 'root', password = '', database = 'PatientApp',charset='utf8')
    with con:
        cur = con.cursor()
        cur.execute("select count(*) from appointments where doctor_name='"+username+"' and appointment_slot='"+slot+"' and appointment_date="+choosen_date)
        rows = cur.fetchall()
        for row in rows:
            count = row[0]
    return count

def BookAppointmentAction(request):
    if request.method == 'POST':
        global userid, slot, slotdate
        choosen_date = request.POST.get('t1', False)
        slot = request.POST.get('t2', False)
        choosen_date = str(datetime.datetime.strptime(choosen_date, "%d-%m-%Y").strftime("'%Y-%m-%d'"))
        print(choosen_date)
        output = '<h4><b>Appointment Booking Screen</b></h4><table border="1" align="center" width="100%" ><tr>'
        slotdate = choosen_date
        font = '<font size="" color="black">'
        columns = ['Doctor Name','Email ID','Contact No','Qualification','Experience Details', 'Availability Status', 'Book Appointment']
        for i in range(len(columns)):
            output += '<th>'+font+columns[i]+'</th>'
        output += "</tr>"    
        con = pymysql.connect(host='127.0.0.1',port = 3306,user = 'root', password = '', database = 'PatientApp',charset='utf8')
        with con:
            cur = con.cursor()
            cur.execute("select username,emailid,contact_no,qualification,experience_details FROM adddoctor")
            rows = cur.fetchall()
            for row in rows:
                username = row[0]
                email = row[1]
                contact = row[2]
                qualification = row[3]
                exp = row[4]
                count = checkSlot(username, slot, choosen_date)
                output+='<tr><td>'+font+str(username)+'</td>'
                output+='<td>'+font+str(email)+'</td>'
                output+='<td>'+font+str(contact)+'</td>'
                output+='<td>'+font+str(qualification)+'</td>'
                output+='<td>'+font+str(exp)+'</td>'
                if count < 6:
                    output+='<td>'+font+"Yes"+'</td>'
                    output+='<td><a href=\'ConfirmAppointment?doctor='+str(username)+'\'><font size=3 color=black>Click Here for Appointment</font></a></td>'
                else:
                    output+='<td>'+font+"No"+'</td>'
                    output+='<td><font size="" color="red">Already Booked</td>'
        context= {'data':output}
        return render(request, 'ViewPatientReports.html', context)            
                    
def ConfirmAppointmentAction(request):
    if request.method == 'POST':
        global userid, slot, slotdate, doctorname
        disease = request.POST.get('t1', False)
        count = 0
        con = pymysql.connect(host='127.0.0.1',port = 3306,user = 'root', password = '', database = 'PatientApp',charset='utf8')
        with con:
            cur = con.cursor()
            cur.execute(" select max(appointment_id) from appointments")
            rows = cur.fetchall()
            for row in rows:
                count = row[0]
        count = count + 1
        db_connection = pymysql.connect(host='127.0.0.1',port = 3306,user = 'root', password = '', database = 'PatientApp',charset='utf8')
        db_cursor = db_connection.cursor()
        student_sql_query = "INSERT INTO appointments(appointment_id,patient_name,disease_description,prescription,appointment_date,appointment_slot,doctor_name) VALUES('"+str(count)+"','"+userid+"','"+disease+"','None',"+slotdate+",'"+slot+"','"+doctorname+"')"
        db_cursor.execute(student_sql_query)
        db_connection.commit()
        print(db_cursor.rowcount, "Record Inserted")
        if db_cursor.rowcount == 1:
            context= {'data':'Appointments details added'}
            return render(request, 'PatientScreen.html', context)
        else:
            context= {'data':'Error in adding appointment details'}
            return render(request, 'PatientScreen.html', context)

def ConfirmAppointment(request):
    if request.method == 'GET':
        global userid, slot, slotdate, doctorname
        doctorname = request.GET['doctor']
        return render(request, 'ConfirmAppointment.html', {})

def ViewMyPatientDetails(request):
    if request.method == 'GET':
        global userid
        output = '<h4><b>Your Details Screen</b></h4><table border="1" align="center" width="100%" ><tr>'
        font = '<font size="" color="black">'
        columns = ['Username','Password','Contact No','Email ID','Address']
        for i in range(len(columns)):
            output += '<th>'+font+columns[i]+'</th>'
        output += "</tr>"    
        con = pymysql.connect(host='127.0.0.1',port = 3306,user = 'root', password = '', database = 'PatientApp',charset='utf8')
        with con:
            cur = con.cursor()
            cur.execute("select * FROM patientsignup where username='"+userid+"'")
            rows = cur.fetchall()
            for row in rows:
                output+='<tr><td>'+font+str(row[0])+'</td>'
                output+='<td>'+font+str(row[1])+'</td>'
                output+='<td>'+font+str(row[2])+'</td>'
                output+='<td>'+font+str(row[3])+'</td>'
                output+='<td>'+font+str(row[4])+'</td>'                
        context= {'data':output}
        return render(request, 'ViewPatientReports.html', context)               
                
def ViewPatientAppointment(request):
    if request.method == 'GET':
        global userid
        output = '<h4><b>Your Appointment Details Screen</b></h4><table border="1" align="center" width="100%" ><tr>'
        font = '<font size="" color="black">'
        columns = ['Appointment ID','Patient Name','Disease Description','Prescription','Appointment Date','Appointment Slot', 'Doctor Name', 'Cancel Booking']
        for i in range(len(columns)):
            output += '<th>'+font+columns[i]+'</th>'
        output += "</tr>"    
        con = pymysql.connect(host='127.0.0.1',port = 3306,user = 'root', password = '', database = 'PatientApp',charset='utf8')
        with con:
            cur = con.cursor()
            cur.execute("select * FROM appointments where patient_name='"+userid+"'")
            rows = cur.fetchall()
            for row in rows:
                output+='<tr><td>'+font+str(row[0])+'</td>'
                output+='<td>'+font+str(row[1])+'</td>'
                output+='<td>'+font+str(row[2])+'</td>'
                output+='<td>'+font+str(row[3])+'</td>'
                output+='<td>'+font+str(row[4])+'</td>'
                output+='<td>'+font+str(row[5])+'</td>'
                output+='<td>'+font+str(row[6])+'</td>'
                if row[3] == 'None':
                    output+='<td><a href=\'CancelAppointment?aid='+str(row[0])+'\'><font size=3 color=black>Click Here to Cancel</font></a></td>'
                else:
                    output+='<td>'+font+"Appointment Completed"+'</td>'
        context= {'data':output}
        return render(request, 'ViewPatientReports.html', context)

def CancelAppointment(request):
    if request.method == 'GET':
        global userid, slot, slotdate, doctorname
        aid = request.GET['aid']
        db_connection = pymysql.connect(host='127.0.0.1',port = 3306,user = 'root', password = '', database = 'PatientApp',charset='utf8')
        db_cursor = db_connection.cursor()
        student_sql_query = "delete from appointments where appointment_id='"+aid+"'"
        db_cursor.execute(student_sql_query)
        db_connection.commit()
        context= {'data':"Appointment Cancelled"}
        return render(request, 'PatientScreen.html', context)

def DonateOrgan(request):
    if request.method == 'GET':
       return render(request, 'DonateOrgan.html', {})    
    

def DonateOrganAction(request):
    if request.method == 'POST':
        global userid
        today = date.today()
        organ = request.POST.get('t1', False)
        desc = request.POST.get('t2', False)
        db_connection = pymysql.connect(host='127.0.0.1',port = 3306,user = 'root', password = '', database = 'PatientApp',charset='utf8')
        db_cursor = db_connection.cursor()
        student_sql_query = "INSERT INTO donateorgans(username,donating_organ,description,donate_date) VALUES('"+str(userid)+"','"+organ+"','"+desc+"','"+str(today)+"')"
        db_cursor.execute(student_sql_query)
        db_connection.commit()
        print(db_cursor.rowcount, "Record Inserted")
        if db_cursor.rowcount == 1:
            context= {'data':'Donating organ details added'}
            return render(request, 'DonateOrgan.html', context)
        else:
            context= {'data':'Error in adding organ details'}
            return render(request, 'DonateOrgan.html', context)



def Feedback(request):
    if request.method == 'GET':
       return render(request, 'Feedback.html', {})    
    

def FeedbackAction(request):
    if request.method == 'POST':
        global userid
        today = date.today()
        feedback = request.POST.get('t1', False)
        db_connection = pymysql.connect(host='127.0.0.1',port = 3306,user = 'root', password = '', database = 'PatientApp',charset='utf8')
        db_cursor = db_connection.cursor()
        student_sql_query = "INSERT INTO feedback(username,feedback,feedback_date) VALUES('"+str(userid)+"','"+feedback+"','"+str(today)+"')"
        db_cursor.execute(student_sql_query)
        db_connection.commit()
        print(db_cursor.rowcount, "Record Inserted")
        if db_cursor.rowcount == 1:
            context= {'data':'Feedback details added'}
            return render(request, 'Feedback.html', context)
        else:
            context= {'data':'Error in adding Feedback details'}
            return render(request, 'Feedback.html', context)

def getuserdetails(username):
    address = ""
    email = ""
    contact = ""
    con = pymysql.connect(host='127.0.0.1',port = 3306,user = 'root', password = '', database = 'PatientApp',charset='utf8')
    with con:
        cur = con.cursor()
        cur.execute("select contact_no,email,address FROM patientsignup where username='"+username+"'")
        rows = cur.fetchall()
        for row in rows:
            contact = row[0]
            email = row[1]
            address = row[2]
    return contact, email, address

def SearchOrgan(request):
    if request.method == 'GET':
        global userid
        output = '<h4><b>Search Organ Details Screen</b></h4><table border="1" align="center" width="100%" ><tr>'
        font = '<font size="" color="black">'
        columns = ['Donar Name','Donating Organ','Description','Donate Date','Address', 'Email ID', 'Contact No']
        for i in range(len(columns)):
            output += '<th>'+font+columns[i]+'</th>'
        output += "</tr>"    
        con = pymysql.connect(host='127.0.0.1',port = 3306,user = 'root', password = '', database = 'PatientApp',charset='utf8')
        with con:
            cur = con.cursor()
            cur.execute("select * FROM donateorgans")
            rows = cur.fetchall()
            for row in rows:
                output+='<tr><td>'+font+str(row[0])+'</td>'
                output+='<td>'+font+str(row[1])+'</td>'
                output+='<td>'+font+str(row[2])+'</td>'
                output+='<td>'+font+str(row[3])+'</td>'
                contact, email, address = getuserdetails(row[0])
                output+='<td>'+font+str(address)+'</td>'
                output+='<td>'+font+str(email)+'</td>'
                output+='<td>'+font+str(contact)+'</td>' 
        context= {'data':output}
        return render(request, 'ViewPatientReports.html', context)  

def ViewDoctorDetails(request):
    if request.method == 'GET':
        global userid
        output = '<h4><b>View Your Details Screen</b></h4><table border="1" align="center" width="100%" ><tr>'
        font = '<font size="" color="black">'
        columns = ['Username','Password','Email ID','Contact No','Qualification', 'Experience Details', 'Hospital Name', 'Address', 'Speciality']
        for i in range(len(columns)):
            output += '<th>'+font+columns[i]+'</th>'
        output += "</tr>"    
        con = pymysql.connect(host='127.0.0.1',port = 3306,user = 'root', password = '', database = 'PatientApp',charset='utf8')
        with con:
            cur = con.cursor()
            cur.execute("select * FROM adddoctor where username='"+userid+"'")
            rows = cur.fetchall()
            for row in rows:
                output+='<tr><td>'+font+str(row[0])+'</td>'
                output+='<td>'+font+str(row[1])+'</td>'
                output+='<td>'+font+str(row[2])+'</td>'
                output+='<td>'+font+str(row[3])+'</td>'
                output+='<td>'+font+str(row[4])+'</td>'
                output+='<td>'+font+str(row[5])+'</td>'
                output+='<td>'+font+str(row[6])+'</td>'
                output+='<td>'+font+str(row[7])+'</td>'
                output+='<td>'+font+str(row[8])+'</td>'
        context= {'data':output}
        return render(request, 'ViewDoctorReports.html', context)

def ViewDoctorAppointment(request):
    if request.method == 'GET':
        global userid
        today = date.today()
        print("toda "+str(today))
        output = '<h4><b>Your Appointment Details Screen</b></h4><table border="1" align="center" width="100%" ><tr>'
        font = '<font size="" color="black">'
        columns = ['Appointment ID','Patient Name','Disease Description','Prescription','Appointment Date','Appointment Slot', 'Doctor Name', 'Generate Prescription']
        for i in range(len(columns)):
            output += '<th>'+font+columns[i]+'</th>'
        output += "</tr>"    
        con = pymysql.connect(host='127.0.0.1',port = 3306,user = 'root', password = '', database = 'PatientApp',charset='utf8')
        with con:
            cur = con.cursor()
            cur.execute("select * FROM appointments where doctor_name='"+userid+"' and appointment_date='"+str(today)+"'")
            rows = cur.fetchall()
            for row in rows:
                output+='<tr><td>'+font+str(row[0])+'</td>'
                output+='<td>'+font+str(row[1])+'</td>'
                output+='<td>'+font+str(row[2])+'</td>'
                output+='<td>'+font+str(row[3])+'</td>'
                output+='<td>'+font+str(row[4])+'</td>'
                output+='<td>'+font+str(row[5])+'</td>'
                output+='<td>'+font+str(row[6])+'</td>'
                if row[3] == 'None':
                    output+='<td><a href=\'GeneratePrescription?aid='+str(row[0])+'\'><font size=3 color=black>Click Here for Prescription</font></a></td>'
                else:
                    output+='<td>'+font+"Prescription Already Generated"+'</td>'
        context= {'data':output}
        return render(request, 'ViewDoctorReports.html', context)

def GeneratePrescription(request):
    if request.method == 'GET':
        global aid
        aid = request.GET['aid']
        return render(request, 'GeneratePrescription.html', {})
        
def GeneratePrescriptionAction(request):
    if request.method == 'POST':
        global aid
        prescription = request.POST.get('t1', False)
        db_connection = pymysql.connect(host='127.0.0.1',port = 3306,user = 'root', password = '', database = 'PatientApp',charset='utf8')
        db_cursor = db_connection.cursor()
        student_sql_query = "update appointments set prescription='"+prescription+"' where appointment_id='"+aid+"'"
        db_cursor.execute(student_sql_query)
        db_connection.commit()
        context= {'data':"Prescription details added"}
        return render(request, 'DoctorScreen.html', context)


def ViewAdminAppointments(request):
    if request.method == 'GET':
        output = '<h4><b>View Appointment Details Screen</b></h4><table border="1" align="center" width="100%" ><tr>'
        font = '<font size="" color="black">'
        columns = ['Appointment ID','Patient Name','Disease Description','Prescription','Appointment Date','Appointment Slot', 'Doctor Name']
        for i in range(len(columns)):
            output += '<th>'+font+columns[i]+'</th>'
        output += "</tr>"    
        con = pymysql.connect(host='127.0.0.1',port = 3306,user = 'root', password = '', database = 'PatientApp',charset='utf8')
        with con:
            cur = con.cursor()
            cur.execute("select * FROM appointments")
            rows = cur.fetchall()
            for row in rows:
                output+='<tr><td>'+font+str(row[0])+'</td>'
                output+='<td>'+font+str(row[1])+'</td>'
                output+='<td>'+font+str(row[2])+'</td>'
                output+='<td>'+font+str(row[3])+'</td>'
                output+='<td>'+font+str(row[4])+'</td>'
                output+='<td>'+font+str(row[5])+'</td>'
                output+='<td>'+font+str(row[6])+'</td>'                
        context= {'data':output}
        return render(request, 'ViewAdminReports.html', context)

def ViewAdminPatients(request):
    if request.method == 'GET':
        output = '<h4><b>Your Patient Details Screen</b></h4><table border="1" align="center" width="100%" ><tr>'
        font = '<font size="" color="black">'
        columns = ['Username','Password','Contact No','Email ID','Address']
        for i in range(len(columns)):
            output += '<th>'+font+columns[i]+'</th>'
        output += "</tr>"    
        con = pymysql.connect(host='127.0.0.1',port = 3306,user = 'root', password = '', database = 'PatientApp',charset='utf8')
        with con:
            cur = con.cursor()
            cur.execute("select * FROM patientsignup")
            rows = cur.fetchall()
            for row in rows:
                output+='<tr><td>'+font+str(row[0])+'</td>'
                output+='<td>'+font+str(row[1])+'</td>'
                output+='<td>'+font+str(row[2])+'</td>'
                output+='<td>'+font+str(row[3])+'</td>'
                output+='<td>'+font+str(row[4])+'</td>'                
        context= {'data':output}
        return render(request, 'ViewAdminReports.html', context) 


def ViewAdminDonors(request):
    if request.method == 'GET':
        output = '<h4><b>View Organ Donate User Screen</b></h4><table border="1" align="center" width="100%" ><tr>'
        font = '<font size="" color="black">'
        columns = ['Username','Donating Organ','Description','Donate Date']
        for i in range(len(columns)):
            output += '<th>'+font+columns[i]+'</th>'
        output += "</tr>"    
        con = pymysql.connect(host='127.0.0.1',port = 3306,user = 'root', password = '', database = 'PatientApp',charset='utf8')
        with con:
            cur = con.cursor()
            cur.execute("select * FROM donateorgans")
            rows = cur.fetchall()
            for row in rows:
                output+='<tr><td>'+font+str(row[0])+'</td>'
                output+='<td>'+font+str(row[1])+'</td>'
                output+='<td>'+font+str(row[2])+'</td>'
                output+='<td>'+font+str(row[3])+'</td>'                          
        context= {'data':output}
        return render(request, 'ViewAdminReports.html', context) 


def ViewAdminFeedback(request):
    if request.method == 'GET':
        output = '<h4><b>View User Feedback Details Screen</b></h4><table border="1" align="center" width="100%" ><tr>'
        font = '<font size="" color="black">'
        columns = ['Username','Feedback',' Date']
        for i in range(len(columns)):
            output += '<th>'+font+columns[i]+'</th>'
        output += "</tr>"    
        con = pymysql.connect(host='127.0.0.1',port = 3306,user = 'root', password = '', database = 'PatientApp',charset='utf8')
        with con:
            cur = con.cursor()
            cur.execute("select * FROM feedback")
            rows = cur.fetchall()
            for row in rows:
                output+='<tr><td>'+font+str(row[0])+'</td>'
                output+='<td>'+font+str(row[1])+'</td>'
                output+='<td>'+font+str(row[2])+'</td>'                                         
        context= {'data':output}
        return render(request, 'ViewAdminReports.html', context)











