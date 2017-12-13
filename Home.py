from flask import Flask, render_template,request,redirect
from firebase import firebase
import firebase_admin
from firebase_admin import credentials, db
from wtforms import Form, SelectField, validators

cred = credentials.Certificate('cred/daryltan-9eddf-firebase-adminsdk-gj8gk-a7e6e9d435.json')
default_app = firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://daryltan-9eddf.firebaseio.com/'
})

root = db.reference()

app = Flask(__name__)

@app.route('/home/')
def home():
    return render_template('home.html')

@app.route('/mt/')
def mt():
    return render_template('/Daryl/mrtTiming.html')

@app.route('/at/')
def at():
    return render_template('/Daryl/alternative_transport.html')

@app.route('/mc/')
def mc():
    return render_template('/MunHong/MrtCrowded.html')

@app.route('/mh/')
def mh():
    return render_template('/MunHong/MrtHappy.html')

class webForm(Form):
    dropDownBox = SelectField('Eg of Dropbox Box', [validators.DataRequired()],
                              choices=[('','< Select Boarding Station >'),('44', 'Admiralty [NS10]'),('34', 'Aljunied [EW9]'),
                                       ('2','Ang Mo Kio [NS16]'),('119','Bakau [SE13]'),('','Bangkit [BP9]'),('','Bartley [CC12]'),
                                       ('','Bayfront [CE1/DT16]'),('','Beauty World [DT5]'),('','Bedok [EW5]'),('','Bedok North [DT29]'),
                                       ('','Bedok Reservoir [DT30]'),('','Bencoolen [DT21]'),('','Bendemeer [DT23]'),('','Bishan [NS17/CC15]'),
                                       ('','Boon Keng [NE9]'),('','Bakau [SE13]'),('','Bakau [SE13]'),('','Bakau [SE13]'),('','Bakau [SE13]'),
                                       ('','Bakau [SE13]'),('','Bakau [SE13]'),('','Bakau [SE13]'),('','Bakau [SE13]'),('','Bakau [SE13]'),
                                       ('','Bakau [SE13]'),('','Bakau [SE13]') ]
                              ,default=''
                              )

    dropDownBox1 = SelectField('Eg of Dropbox Box', [validators.DataRequired()],
                              choices=[('', '< Select Boarding Station >'), ('34', 'Aljunied'), ('2', 'Ang Mo Kio')],
                              default=''
                              )
@app.route('/routes/', methods=["GET","POST"])
def routes():
    form=webForm(request.form)
    if request.method=="POST" and form.validate():
        x=form.dropDownBox.data
        y=form.dropDownBox1.data
        print(x)
        print(y)
        return redirect("routes")
    return render_template('/JunLoong/MRT_Routes.html',form=form)

@app.route('/my-link/')
def my_link():
  return render_template('/MunHong/MrtCrowdedFunction.py')

@app.route("/submit", methods=["POST"])
def submit():
    return render_template("home.html")
if __name__ == '__main__':
    app.secret_key = 'secret123'
    app.run(debug=True)


