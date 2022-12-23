from pprint import pprint
from flask import *
from database import *

import smtplib
from email.mime.text import MIMEText
from flask_mail import Mail

api=Blueprint('api',__name__)

@api.route('/login')
def login():
    data={}
    un=request.args['username']
    pwd=request.args['password']
    print(un,pwd)
    z="select * from `login` where username='%s' and password='%s' "%(un,pwd)
    res=select(z)

    if res:
        data['status']='success'
        data['data']=res
    else:
        data['status']='failed'
    return str(data)



@api.route("/blooddonation")
def blooddonation():
    data={}
    lid=request.args['log_id']
    blood=request.args['blooddetails']

    q="select * from donor where donor_id=(select donor_id from donor where login_id='%s')"%(lid)
    val=select(q)
    name=val[0]['first_name']+val[0]['last_name']
    gender=val[0]['gender']
    age=val[0]['age']
    pin=val[0]['pincode']
    phn=val[0]['phone']
    em=val[0]['email']

    q="select email from organization"
    res=select(q)
    for i in res:
        emailid=i['email']
        email=emailid
        print(email)

       

        pwd="Name : "+name+"\nGender : "+gender+"\nAge : "+age+"\nPincode : "+pin+"\nPhone no : "+phn+"\nEmail id : "+em
     
        try:
            gmail = smtplib.SMTP('smtp.gmail.com', 587)
            gmail.ehlo()
            gmail.starttls()
            gmail.login('sngistoutpass@gmail.com','izgqjuqneorhokje')
        except Exception as e:
            print("Couldn't setup email!!"+str(e))

        pwd = MIMEText(pwd)

        pwd['Subject'] = 'i AM INTRESTED IN BLOOD DONATION.'

        pwd['To'] = email

        pwd['From'] = 'sngistoutpass@gmail.com'

        try:
            gmail.send_message(pwd)
   
            flash("EMAIL SENED SUCCESFULLY")
            


        except Exception as e:
            print("COULDN'T SEND EMAIL", str(e))
        else:
            flash("INVALID DETAILS")
        flash('ADDED...')


    q="insert into donation values(null,(select donor_id from donor where login_id='%s' ),'blood','%s','pending')"%(lid,blood)
    res=insert(q)

    if res:
        data['status']='success'
    return str(data)

@api.route("/organdonation")
def organdonation():
    data={}
    lid=request.args['log_id']
    organ=request.args['organdetails']
    q="select * from donor where donor_id=(select donor_id from donor where login_id='%s')"%(lid)
    val=select(q)
    name=val[0]['first_name']+val[0]['last_name']
    gender=val[0]['gender']
    age=val[0]['age']
    pin=val[0]['pincode']
    phn=val[0]['phone']
    em=val[0]['email']

    q="select email from organization"
    res=select(q)
    for i in res:
        emailid=i['email']
        email=emailid
        print(email)

       

        pwd="Name : "+name+"\nGender : "+gender+"\nAge : "+age+"\nPincode : "+pin+"\nPhone no : "+phn+"\nEmail id : "+em
     
        try:
            gmail = smtplib.SMTP('smtp.gmail.com', 587)
            gmail.ehlo()
            gmail.starttls()
            gmail.login('sngistoutpass@gmail.com','izgqjuqneorhokje')
        except Exception as e:
            print("Couldn't setup email!!"+str(e))

        pwd = MIMEText(pwd)

        pwd['Subject'] = 'i AM INTRESTED IN ORGAN dONATION.'

        pwd['To'] = email

        pwd['From'] = 'sngistoutpass@gmail.com'

        try:
            gmail.send_message(pwd)
   
            flash("EMAIL SENED SUCCESFULLY")
            


        except Exception as e:
            print("COULDN'T SEND EMAIL", str(e))
        else:
            flash("INVALID DETAILS")
        flash('ADDED...')

    q="insert into donation values(null,(select donor_id from donor where login_id='%s' ),'organ','%s','pending')"%(lid,organ)
    res=insert(q)
    if res:
        data['status']='success' 
    return str(data)

@api.route('/vieworgans')
def vieworgans():
    data={}
    q="select * from organ"
    res=select(q)
    if res:
        data['status']='success'
        data['data']=res
    return str(data)

@api.route('/viewblood')
def viewblood():
    data={}
    q="select * from bloodgroups"
    res=select(q)
    if res:
        data['method']='viewblood'
        data['data']=res
    return str(data)


@api.route('/vieworgan')
def vieworgan():
    data={}
    q="select * from organ"
    res=select(q) 
    if res:
        data['method']='vieworgan'
        data['data']=res
    return str(data)


@api.route('/viewrequsets')
def viewrequsets():
    data={}
    logid=request.args['log_id']
    q="select * from blood_requests inner join bloodgroups using(group_id) where receiver_id=(select receiver_id from receiver where login_id='%s')"%(logid)

    res=select(q) 
    if res:
        data['status']='success'
        data['data']=res
    return str(data)


@api.route('/addorgan')
def addorgan():
    data={}
    logid=request.args['log_id']
    dateval=request.args['date']
    print(dateval)
    # date=str(dateval)
    orgid=request.args['orgid']

    q="select organ_name from organ where organ_id='%s'"%(orgid)
    orgval=select(q)
    org_name=orgval[0]['organ_name']

    q="select * from receiver where receiver_id=(select receiver_id from receiver where login_id='%s')"%(logid)
    val=select(q)
    name=val[0]['first_name']+val[0]['last_name']
    place=val[0]['place']
    statee=val[0]['state']
    pin=val[0]['pincode']
    phn=val[0]['phone']
    em=val[0]['email']

    q="select email from organization"
    res=select(q)
    for i in res:
        emailid=i['email']
        email=emailid
        print(email)

       

        pwd="Name : "+name+"\nPlace : "+place+"\nState : "+statee+"\nPincode : "+pin+"\nPhone no : "+phn+"\nEmail id : "+em +"\nRequired Organ : "+org_name +"\nRequired Date : "+dateval
     
        try:
            gmail = smtplib.SMTP('smtp.gmail.com', 587)
            gmail.ehlo()
            gmail.starttls()
            gmail.login('sngistoutpass@gmail.com','izgqjuqneorhokje')
        except Exception as e:
            print("Couldn't setup email!!"+str(e))

        pwd = MIMEText(pwd)

        pwd['Subject'] = 'REQUEST FOR ORGAN !'

        pwd['To'] = email

        pwd['From'] = 'sngistoutpass@gmail.com'

        try:
            gmail.send_message(pwd)
   
            flash("EMAIL SENED SUCCESFULLY")
            


        except Exception as e:
            print("COULDN'T SEND EMAIL", str(e))
        else:
            flash("INVALID DETAILS")
        flash('ADDED...')

    q="insert into organ_request values (null,(select receiver_id from receiver where login_id='%s'),'%s',curdate(),'pending','%s')"%(logid,orgid,dateval)
    print(q)
    res=insert(q)
    if res:
        data['method']='addorgan'
        data['data']=res
    return str(data)

@api.route('/addblood')
def addblood():
    data={}
    logid=request.args['log_id']
    dateval=request.args['date']
    groupid=request.args['groupid']
    quantity=request.args['quantity']
    pincode=request.args['pincode']

    q="select group_name from bloodgroups where group_id='%s'"%(groupid)
    groupval=select(q)
    groupname=groupval[0]['group_name']

    q="select * from receiver where receiver_id=(select receiver_id from receiver where login_id='%s')"%(logid)
    val=select(q)
    name=val[0]['first_name']+val[0]['last_name']
    place=val[0]['place']
    statee=val[0]['state']
    pin=val[0]['pincode']
    phn=val[0]['phone']
    em=val[0]['email']

    q="select email from organization"
    res=select(q)
    for i in res:
        emailid=i['email']
        email=emailid
        print(email)

       

        pwd="Name : "+name+"\nPlace : "+place+"\nState : "+statee+"\nPincode : "+pin+"\nPhone no : "+phn+"\nEmail id : "+em +"\nRequired Blood group : "+groupname +"\nRequired Date : "+dateval+"\nRequired Quantity : "+quantity +"\nPincode : "+pincode
     
        try:
            gmail = smtplib.SMTP('smtp.gmail.com', 587)
            gmail.ehlo()
            gmail.starttls()
            gmail.login('sngistoutpass@gmail.com','izgqjuqneorhokje')
        except Exception as e:
            print("Couldn't setup email!!"+str(e))

        pwd = MIMEText(pwd)

        pwd['Subject'] = 'REQUEST FOR Blood !'

        pwd['To'] = email

        pwd['From'] = 'sngistoutpass@gmail.com'

        try:
            gmail.send_message(pwd)
   
            flash("EMAIL SENED SUCCESFULLY")
            


        except Exception as e:
            print("COULDN'T SEND EMAIL", str(e))
        else:
            flash("INVALID DETAILS")
        flash('ADDED...')
    q="insert into blood_requests values (null,(select receiver_id from receiver where login_id='%s'),'%s',curdate(),%s,'%s','pending','%s')"%(logid,groupid,quantity,pincode,dateval)

    print(q)
    res=insert(q)
    if res:
        data['method']='addblood'
        data['data']=res
    return str(data)

@api.route('/vieworganrequest')
def vieworganrequest():
    data={}
    logid=request.args['log_id']
    q="select * from organ_request inner join organ using(organ_id) where receiver_id=(select receiver_id from receiver where login_id='%s')"%(logid)

    res=select(q) 
    if res:
        data['status']='success'
        data['data']=res
    return str(data)

@api.route('/donorreqmessage')
def donorreqmessage():
    data={}
    # logid=request.args['log_id']
    q="select * from blood_requirement_message inner join organization using (organization_id) inner join bloodgroups using (group_id) where status='pending'"
    res=select(q)

    if res:
        data['mid']=res[0]['message_id']
        data['method']='donorreqmessage'
        data['status'] ='failed'
        data['data']=res
    else:
        data['status'] ='failed'
    return str(data)

@api.route("/donorupdatestatus")
def donorupdatestatus():
    data={}
    logid=request.args['log_id']
    mid=request.args['mid']

    q="update blood_requirement_message set donor_id=(select donor_id from donor where login_id='%s') , status='accepted by donor' where message_id='%s'"%(logid,mid)
    update(q)

    data['method']='donorupdatestatus'
    return str(data)

@api.route("/donatedhistory")
def donatedhistory():
    data={}
    logid=request.args['log_id']
    q="select * from donation where status='donation completed' and donor_id=(select donor_id from donor where login_id='%s')"%(logid)
    # print(q)
    res=select(q)
    if res:
        data['status']='success'
        data['data']=res
    return str(data)



@api.route("/remaninghistory")
def remaninghistory():
    data={}
    logid=request.args['log_id']
    q="select * from donation where status='accepted by donor' and donor_id=(select donor_id from donor where login_id='%s')"%(logid)
    # print(q)
    res=select(q)
    if res:
        data['status']='success'
        data['data']=res
    return str(data)

@api.route("/donreg",methods=['get','post'])
def donreg():
    data={}

    fname=request.args['fname']
    lname=request.args['lname']
    age=request.args['age']
    email=request.args['email']
    gender=request.args['gender']
    phone=request.args['phone']
    group_id=request.args['group_id']
    pin=request.args['pincode']

    username=request.args['username']
    password=request.args['password']

    q="select * from login where username='%s' and password='%s'"%(username,password)
    rep=select(q)

    if rep:
        data['status']='already'
        data['method']='donreg'
    else:
        q="insert into `login` values(NULL,'%s','%s','donor') "%(username,password)
        ref=insert(q)
        v="insert into `donor` values(NULL,'%s','%s','%s','%s','%s','%s','%s','%s','%s') "%(ref,fname,lname,group_id,gender,age,pin,phone,email)
        insert(v)
        data['status']='success'
        data['method']='donreg'
    return str(data)

@api.route("/receiverreg",methods=['get','post'])
def receiverreg():
    data={}

    fname=request.args['fname']
    lname=request.args['lname']
    hname=request.args['housename']
    place=request.args['place']
    pincode=request.args['pincode']
    phone=request.args['phone']

    state=request.args['state']
    email=request.args['email']

    username=request.args['username']
    password=request.args['password']

    q="select * from login where username='%s' and password='%s'"%(username,password)
    rep=select(q)

    if rep:
        data['status']='already'
    else:
        q="insert into `login` values(NULL,'%s','%s','receiver') "%(username,password)
        ref=insert(q)
        v="insert into `receiver` values(NULL,'%s','%s','%s','%s','%s','%s','%s','%s','%s') "%(ref,fname,lname,hname,place,pincode,phone,state,email)

        insert(v)
        data['status']='success'
    return str(data)

@api.route('/recchangepass')
def recchangepass():
    data={}
    curpas=request.args['curpas']
    newpas=request.args['newpas']
    confpas=request.args['confpas']
    lid=request.args['log_id']

    q="select * from login where loginid='%s' and password='%s'"%(lid,curpas)
    res=select(q)

    if res:
        if newpas == confpas:
            q="update login set password='%s' where loginid='%s'"%(newpas,lid)
            update(q)
            data['status']='success'
        else:
            data['status']='mismatch'
    else:
        data['status']='failed'


    return str(data)

@api.route('/donchangepass')
def donchangepass():
    data={}
    curpas=request.args['curpas']
    newpas=request.args['newpas']
    confpas=request.args['confpas']
    lid=request.args['log_id']

    q="select * from login where loginid='%s' and password='%s'"%(lid,curpas)
    res=select(q)

    if res:
        if newpas == confpas:
            q="update login set password='%s' where loginid='%s'"%(newpas,lid)
            update(q)
            data['status']='success'
        else:
            data['status']='mismatch'
    else:
        data['status']='failed'


    return str(data)



@api.route('/viewbloodtype')
def viewbloodtype():
    data={}
    q="select * from bloodgroups"
    res=select(q) 
    if res:
        data['method']='viewbloodtype'
        data['data']=res
        data['status']='success'
    return str(data)



@api.route('/vieworgreqdonor')
def vieworgreqdonor():
    data={}
    lid=request.args['log_id']
    q="SELECT * FROM donation INNER JOIN donor USING (donor_id) INNER JOIN `organization` USING (`organization_id`) where donor_id=(select donor_id from donor where login_id='%s') "%(lid)
    
    res=select(q) 
    if res:
        data['method']='vieworgreqdonor'
        data['data']=res
        data['status']='success'
    return str(data)