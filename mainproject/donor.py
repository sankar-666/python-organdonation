from flask import Flask,Blueprint,render_template

donor=Blueprint('donor',__name__)

@donor.route('/donor',methods=['post','get'])
def donorhome():
    return render_template('donorhome.html')

@donor.route('/donsendreq',methods=['post','get'])
def donreq():
    return render_template('senddonation.html')