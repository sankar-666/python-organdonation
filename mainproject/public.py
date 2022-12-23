from flask import *
from database import *

public=Blueprint('public',__name__)
@public.route('/')
def home():
    return render_template("home.html")

#ADMIN_LOGIN

@public.route('/login', methods=['post','get'])
def login():
    if 'submit' in request.form:
        un=request.form['username']
        pwd=request.form['password']
        # userval=request.form['userval']
        # passval=request.form['passval']
        print("sahudhgsaudghsajhdbuashbduasbd")
        # print(userval,passval)
        print(un,pwd)
        q="select * from login where username='%s' and password='%s'"%(un,pwd)
        res=select(q)
        if res:
            session['logid']=res[0]['loginid']
            utype=res[0]['usertype']
            print(utype)
            if utype=="admin":
                return redirect(url_for('admin.adminhome'))
            elif utype=="Organization":
                q="select * from organization where loginid='%s'"%(session['logid'])
                res=select(q)
                if res:
                    session['org_id']=res[0]['organization_id']
                return redirect(url_for('organization.organizationhome'))
        else:
            flash("Invalid Username or Password")
    return render_template("login.html")

#ORGANIZATION_REGISTER
@public.route('/registerorg',methods=['post','get'])
def registerorg():
    if 'submit' in request.form:
        n=request.form['name']
        pl=request.form['place']
        pin=request.form['pin']
        ph=request.form['phone']
        m=request.form['mail']
        lno=request.form['lno']
        un=request.form['username']
        pwd=request.form['password']
        print(n,un,ph,pl,pin,pwd,m,lno)
        q="insert into login values(NULL,'%s','%s','pending')"%(un,pwd)
        lid=insert(q)
        r="insert into organization values(NULL,'%s','%s','%s','%s','%s','%s','%s')"%(lid,n,pl,pin,ph,m,lno)
        insert(r)
        return redirect(url_for('public.login'))
    
    return render_template("orgreg.html")

#RECEIVEREGISTER
@public.route('/registerreceiver',methods=['get','post'])
def registerreceiver():
    
    if 'submit' in request.form:
        fn=request.form['fname']
        ln=request.form['lname']
        hn=request.form['hname']
        pl=request.form['place']
        pin=request.form['pin']
        state=request.form['state']
        ph=request.form['phone']
        m=request.form['mail']
        un=request.form['username']
        pwd=request.form['password']
        print(fn,un,hn,ph,pl,state,pin,pwd,m)
        q="insert into login values(NULL,'%s','%s','receiver')"%(un,pwd)
        lid=insert(q)
        r="insert into receiver values(NULL,'%s','%s','%s','%s','%s','%s','%s','%s','%s')"%(lid,fn,ln,hn,pl,pin,ph,state,m)
        insert(r)
        return redirect(url_for('public.login'))
    return render_template('receiverreg.html')

#DonorREgister
@public.route('/registerdonor',methods=['get','post'])
def registerdonor():
    data={}
    q="select * from bloodgroups"
    res=select(q)
    data['don']=res
    if 'submit' in request.form:
        fn=request.form['fn']
        ln=request.form['ln']
        bg=request.form['donor']
        gen=request.form['gen']
        age=request.form['age']
        pin=request.form['pin']
        ph=request.form['pn']
        m=request.form['mail']
        un=request.form['username']
        pwd=request.form['password']
        print(fn,ln,un,bg,ph,gen,age,pin,pwd,m)
        q="insert into login values(NULL,'%s','%s','donor')"%(un,pwd)
        lid=insert(q)
        r="insert into donor values(NULL,'%s','%s','%s','%s','%s','%s','%s','%s','%s')"%(lid,fn,ln,bg,gen,age,pin,ph,m)
        insert(r)
        return redirect(url_for('public.login'))
    return render_template('donorreg.html',data=data) 