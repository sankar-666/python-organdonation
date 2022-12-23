from flask import Flask,Blueprint,render_template,request,redirect,url_for
from database import *

admin=Blueprint('admin',__name__)

@admin.route('/adminhome')
def adminhome():
    return render_template('adminhome.html')

@admin.route('/managebloodgrp',methods=['get','post'])
def adminmngbg():
       
     if 'submit' in request.form:
        gn=request.form['grn']
        gd=request.form['grd']
        print(gn,gd)
        q="insert into bloodgroups values(NULL,'%s','%s')"%(gn,gd)
        insert(q)
        return redirect(url_for('admin.adminmngbg'))
     return render_template('adminmngbgroup.html')
 
 
 #view
@admin.route('/bgview',methods=['get','post'])
def bgview():
    data={}
    q="select * from bloodgroups"
    res=select(q)
    data['c']=res
    
    
    if 'action' in request.args:
        id=request.args['id']
        action=request.args['action']
    else:
        action=None
    if action=="delete":

        d="delete from bloodgroups where group_id='%s'"%(id)
        delete(d)
        return redirect(url_for('admin.bgview'))
    if action=='edit':
        e="select * from bloodgroups where group_id='%s'"%(id)
        res=select(e)
        data['r']=res

    if 'update' in request.form:
        gn=request.form['grn']
        gd=request.form['grd']
        print(gn,gd)
        u="update bloodgroups SET group_name='%s', group_description='%s' where group_id='%s'"%(gn,gd,id)
        update(u)
        return redirect(url_for('admin.bgview'))

    return render_template("bgview.html",data=data)




#OrganREg

@admin.route('/manageorgn',methods=['get','post'])
def orgnreg():
       
     if 'submit' in request.form:
        on=request.form['orgnn']
        od=request.form['orgnd']
        print(on,od)
        q="insert into organ values(NULL,'%s','%s')"%(on,od)
        insert(q)
        return redirect(url_for('admin.orgnreg'))
     return render_template('adminorgnmng.html')
 
 
 
 
 #organ view
 
@admin.route('/orgnview',methods=['get','post'])
def orgnview():
    data={}
    q="select * from organ"
    res=select(q)
    data['c']=res
    
    if 'action' in request.args:
        id=request.args['id']
        action=request.args['action']
    else:
        action=None
    if action=="delete":

        d="delete from organ where organ_id='%s'"%(id)
        delete(d)
        return redirect(url_for('admin.orgnview'))
    if action=='edit':
        e="select * from organ where organ_id='%s'"%(id)
        res=select(e)
        data['r']=res

    if 'update' in request.form:
        on=request.form['orgnn']
        od=request.form['orgnd']
        print(on,od)
        u="update organ SET organ_name='%s', organ_details='%s' where organ_id='%s'"%(on,od,id)
        update(u)
        return redirect(url_for('admin.orgnview'))
    return render_template("orgnview.html",data=data)

#receiverView

@admin.route('/recview',methods=['get','post'])
def recview():
    data={}
    q="select * from receiver"
    res=select(q)
    data['c']=res
    return render_template("recview.html",data=data)


#ViewDonor

@admin.route('/donview',methods=['get','post'])
def doniew():
    data={}
    q="select * from donor inner join bloodgroups using(group_id)"
    res=select(q)
    data['c']=res
    return render_template("donview.html",data=data)

#organization view
@admin.route('/organizationview',methods=['post','get'])
def vieworg():
    data={}
    q="SELECT * FROM login INNER JOIN organization USING (loginid)"
    res=select(q)
    data['c']=res
    if "action" in request.args:
        action=request.args['action']
        id=request.args['id']
    else:
        action=None
    if action=="reject":
        a="update login set usertype='rejected' where loginid='%s'"%(id)
        update(a)
        return redirect(url_for('admin.vieworg'))
        
    if action=="accept":
        a="update login set usertype='Organization' where loginid='%s'"%(id)
        update(a)
        return redirect(url_for('admin.vieworg'))

    return render_template("organizationview.html",data=data)


@admin.route('/requestview',methods=['get','post'])
def bldreqview():
    data={}
    q="SELECT *,`blood_requests`.`pincode` AS pin FROM `blood_requests` INNER JOIN `bloodgroups` USING(group_id) INNER JOIN `receiver` USING(receiver_id)"
    res=select(q)
    data['c']=res

    r="SELECT * FROM `organ_request` INNER JOIN `organ` USING(organ_id) INNER JOIN `receiver` USING(receiver_id)"
    res=select(r)
    data['b']=res
    return render_template("adminviewrequest.html",data=data)



@admin.route('/admin_view_donation_report',methods=['get','post'])
def admin_view_donation_report():
    data={}
    return render_template("admin_view_donation_report.html",data=data)