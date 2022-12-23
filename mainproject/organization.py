from flask import *
from database import * 

organization=Blueprint('organization',__name__)

@organization.route('/organization',methods=['post','get'])
def organizationhome():
    return render_template("organizationhome.html")


@organization.route('/organization_view_blood_group',methods=['post','get'])
def organization_view_blood_group():
	data={}
	q="select * from bloodgroups"
	res=select(q)
	data['blood']=res
	return render_template("organization_view_blood_group.html",data=data)


@organization.route('/organization_view_organ_type',methods=['post','get'])
def organization_view_organ_type():
	data={}
	q="select * from organ"
	res=select(q)
	data['org']=res
	return render_template("organization_view_organ_type.html",data=data)



@organization.route('/organization_view_donors',methods=['post','get'])
def organization_view_donors():
	data={}
	q="select * from donor inner join bloodgroups using(group_id)"
	res=select(q)
	data['don']=res
	return render_template("organization_view_donors.html",data=data)


@organization.route('/organization_view_organ_request',methods=['post','get'])
def organization_view_organ_request():
	data={}
	id=request.args['id']
	q="SELECT * FROM `donation` where donation_type='organ' and donor_id='%s'"%(id)
	res=select(q)
	data['org']=res
	return render_template("organization_view_organ_request.html",data=data)


@organization.route('/organization_view_blood_request',methods=['post','get'])
def organization_view_blood_request():
	data={}
	id=request.args['id']
	q="SELECT * FROM `donation` where donation_type='blood' and donor_id='%s'"%(id)
	res=select(q)
	data['org']=res
	return render_template("organization_view_blood_request.html",data=data)


@organization.route('/organization_send_blood_requirement_msg',methods=['post','get'])
def organization_send_blood_requirement_msg():
	data={}
	org=session['org_id']
	q="select * from donor"
	rs=select(q)
	data['don']=rs

	q="select * from bloodgroups"
	res=select(q)
	data['bg']=res

	if 'submit' in request.form:
		don=request.form['don']
		bg=request.form['bg']
		unit=request.form['unit']
		des=request.form['des']
		q="insert into blood_requirement_message values(null,'%s','%s','%s','%s','%s','pending')"%(org,don,bg,unit,des)
		insert(q)
		flash("added successfully")
		return redirect(url_for('organization.organization_send_blood_requirement_msg'))

	q="SELECT * FROM `blood_requirement_message` INNER JOIN `bloodgroups` USING(group_id) INNER JOIN `donor` USING(donor_id) where organization_id='%s'"%(org)
	res=select(q)
	data['req']=res
	return render_template("organization_send_blood_requirement_msg.html",data=data)



@organization.route('/organization_manage_donation',methods=['post','get'])
def organization_manage_donation():
	data={}
	org=session['org_id']
	q="select * from donor"
	rs=select(q)
	data['don']=rs

	q="select * from bloodgroups"
	res=select(q)
	data['bg']=res

	if 'submit' in request.form:
		don=request.form['don']
		bg=request.form['bg']
		unit=request.form['unit']
		q="insert into collection values(null,'%s','%s','%s',now(),'%s')"%(org,don,bg,unit)
		insert(q)
		return redirect(url_for('organization.organization_manage_donation'))
	return render_template("organization_manage_donation.html",data=data)



@organization.route('/organization_view_request',methods=['post','get'])
def organization_view_request():
	data={}
	q="SELECT * FROM  `blood_requests`  INNER JOIN `bloodgroups` USING(group_id) INNER JOIN `receiver` USING(receiver_id)"
	res=select(q)
	data['blood']=res



	q="SELECT * FROM `organ_request` INNER JOIN `organ` USING(organ_id) inner join receiver using(receiver_id)"
	res=select(q)
	data['organ']=res


	if 'action' in request.args:
		action=request.args['action']
		bid=request.args['bid']
		oid=request.args['oid']
		data['bid']=bid
		data['oid']=oid

	else:
		action=None

	if action=="organization_confirm_organ_request":
		q="update organ_request set status='confirm' where organ_request_id='%s'"%(oid)
		update(q)
		return redirect(url_for('organization.organization_view_request'))

	if action=="organization_confirm_blood_request":
		q="update blood_requests set status='confirm' where request_id='%s'"%(bid)
		update(q)
		return redirect(url_for('organization.organization_view_request'))
	return render_template("organization_view_request.html",data=data)