from flask import Flask,Blueprint,render_template

receiver=Blueprint('receiver',__name__)


@receiver.route('/receiverhome',methods=['post'])
def receiverhome():
    return render_template('receiverhome.html')