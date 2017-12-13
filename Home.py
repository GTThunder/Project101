from flask import Flask, render_template,request,redirect,url_for
from firebase import firebase
import firebase_admin
from firebase_admin import credentials, db
from wtforms import SelectField,validators,Form
import numpy as np
from pandas import DataFrame
import matplotlib.pyplot as plt

firebase = \
    firebase.FirebaseApplication('https://daryltan-9eddf.firebaseio.com/', None)
cred = credentials.Certificate('cred/daryltan-9eddf-firebase-adminsdk-gj8gk-a7e6e9d435.json')
default_app = firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://daryltan-9eddf.firebaseio.com/'
})

class MrtCrowded(Form):
    x = SelectField('Which MRT',[validators.DataRequired()],choices=[("Admaralty","Admaralty"),("Yishun","Yishun")])
    y = SelectField('Which Carriage',[validators.DataRequired()],choices=[("Door 1-4", "Door 1-4"), ("Door 5-8", "Door 5-8")])
root = db.reference()

# class MrtHappy(Form):
#     username = StringField('Username', [validators.DataRequired()])
#     password = PasswordField('Password', [validators.DataRequired()])


app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/mt/')
def mt():
    return render_template('/Daryl/mrtTiming.html')

@app.route('/at/')
def at():
    return render_template('/Daryl/alternative_transport.html')

@app.route('/mc/', methods=["POST","GET"])
def mc():
    form = MrtCrowded(request.form)
    if request.method == 'POST' and form.validate():
        y = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
        x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29,
             30,
             31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44]

        df = DataFrame(abs(np.random.randn(7, 44)), index=y, columns=x)

        plt.pcolor(df)
        plt.yticks(np.arange(0.5, len(df.index), 1), df.index)
        plt.xticks(np.arange(0.5, len(df.columns), 1), df.columns)
        plt.show()
    return render_template('MrtCrowded.html', form=form)

@app.route('/surveyInfo', methods=["POST"])
def surveyInfo():
    userResults = {
        "name" : request.form["ownername"],
        "email" : request.form["owneremail"]
    }
    firebase.post("/userAnswers", userResults)
    return redirect(url_for("mh"))


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm(request.form)
    if request.method == 'POST' and form.validate():
        username = form.username.data
        password = form.password.data

        if username == 'admin' and password == 'P@ssw0rd':  # harcoded username and password
            session['logged_in'] = True  # this is to set a session to indicate the user is login into the system.
            return redirect(url_for('viewpublications'))
        else:
            error = 'Invalid login'
            flash(error, 'danger')
            return render_template('Login.html', form=form)

    return render_template('Login.html', form=form)

@app.route('/mh/')
def mh():
    return render_template('/MrtHappy.html')

@app.route('/routes/')
def routes():
    return render_template('/JunLoong/MRT_Routes.html')

@app.route('/my-link/')
def my_link():
    return render_template('/MunHong/MrtCrowdedFunction.html')

if __name__ == '__main__':
    app.secret_key = 'secret123'

    app.run(debug=True)


