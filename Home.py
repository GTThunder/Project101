from flask import Flask, render_template,request,redirect,url_for
from firebase import firebase
import firebase_admin
from firebase_admin import credentials, db
from wtforms import SelectField,validators,Form
import numpy as np
from pandas import DataFrame
import matplotlib.pyplot as plt

firebase = firebase.FirebaseApplication('https://daryltan-9eddf.firebaseio.com/', None)

cred = credentials.Certificate('cred/daryltan-9eddf-firebase-adminsdk-gj8gk-a7e6e9d435.json')
# cred = credentials.Certificate('cred/daryltan-9eddf-firebase-adminsdk-gj8gk-a7e6e9d435.json')
default_app = firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://daryltan-9eddf.firebaseio.com/'
})

class MrtCrowded(Form):
    x = SelectField('Which MRT',[validators.DataRequired()],choices=[("Admiralty","Admiralty"),("Yishun","Yishun")])
    y = SelectField('Which Carriage',[validators.DataRequired()],choices=[("Door 1-4", "Door 1-4"), ("Door 5-8", "Door 5-8")])
root = db.reference()

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

@app.route('/me/')
def me():
    return render_template('/MrtEthics.html')

@app.route('/mh/')
def mh():
    return render_template('/MrtHappy.html')

@app.route('/ma/')
def ma():
    return render_template('/MrtAnswers.html')

@app.route('/submit_userInformation', methods=["POST"])
def submit_userInformation():
    userAnswers = {
        "name" : request.form["ownername"],
        "email" : request.form["owneremail"]
    }
    firebase.post("/userInformationGet", userAnswers)
    return redirect(url_for("ma"))

@app.route('/userInformationGet')
def userInformationGet():
    result = firebase.get("/userInformationGet", None)
    return render_template("MrtEthicsResult.html", userInformationGet = result)


class webForm(Form):
    dropDownBox = SelectField('Eg of Dropbox Box', [validators.DataRequired()],
                              choices=[('', '< Select Boarding Station >'),('0', 'Jurong East [NS1/EW24]'),('3', 'Bukit Batok [NS2]'),
                                    ('5', 'Bukit Gombak [NS3]'),('9', 'Choa Chu Kang [NS4/BP1]'),('11', 'Yew Tee [NS5]'),('16', 'Kranji [NS7]'),
                                    ('18', 'Marsiling [NS8]'),('21', 'Woodlands [NS9]'),('23', 'Admiralty [NS10]'),('26', 'Sembawang [NS11]'),('30', 'Yishun [NS13]'),
                                    ('32', 'Khatib [NS14]'),('38', 'Yio Chu Kang [NS15]'),('40', 'Ang Mo Kio [NS16]'),('42', 'Bishan [NS17/CC15]'),
                                    ('44', 'Braddell [NS18]'),('46', 'Toa Payoh [NS19]'),('48', 'Novena [NS20]'),('50', 'Newton [NS21/DT11]'),('52', 'Orchard [NS22]'),
                                    ('54', 'Somerset [NS23]'),('55', 'Dhoby Ghaut [NS24/NE6/CC1'),('57', 'City Hall [NS25/EW13]'),('59', 'Raffles Place [NS26/EW14]'),
                                    ('61', 'Marina Bay [NS27/CE2]'),('63', 'Marina South Pier [NS28]')], default='')

    dropDownBox1 =SelectField('Eg of Dropbox Box', [validators.DataRequired()],
                              choices=[('', '< Select Alighting Station >'), ('0', 'Jurong East [NS1/EW24]'),
                                       ('3', 'Bukit Batok [NS2]'),
                                       ('5', 'Bukit Gombak [NS3]'), ('9', 'Choa Chu Kang [NS4/BP1]'),
                                       ('11', 'Yew Tee [NS5]'), ('16', 'Kranji [NS7]'),
                                       ('18', 'Marsiling [NS8]'), ('21', 'Woodlands'), ('23', 'Admiralty [NS10]'),
                                       ('26', 'Sembawang [NS11]'), ('30', 'Yishun [NS13]'),
                                       ('32', 'Khatib [NS14]'), ('38', 'Yio Chu Kang [NS15]'),
                                       ('40', 'Ang Mo Kio [NS16]'), ('42', 'Bishan [NS17/CC15]'),
                                       ('44', 'Braddell [NS18]'), ('46', 'Toa Payoh [NS19]'), ('48', 'Novena [NS20]'),
                                       ('50', 'Newton [NS21/DT11]'), ('52', 'Orchard [NS22]'),
                                       ('54', 'Somerset [NS23]'), ('55', 'Dhoby Ghaut [NS24/NE6/CC1'),
                                       ('57', 'City Hall [NS25/EW13]'), ('59', 'Raffles Place [NS26/EW14]'),
                                       ('61', 'Marina Bay [NS27/CE2]'), ('63', 'Marina South Pier [NS28]')], default='')


numValue = ''
@app.route('/routes/', methods=["GET","POST"])
def routes():
    form=webForm(request.form)
    if request.method=="POST" and form.validate():
        x = form.dropDownBox.data
        y = form.dropDownBox1.data
        est = int(x) - int(y)
        if est > 0:
            numValue = est
            print(numValue)
        elif est < 0:
            numValue = est * -1
            print(numValue)
        return render_template('JunLoong/MRT_Table.html', given_value=numValue)
        # return redirect(url_for("table"))
    return render_template('JunLoong/MRT_Routes.html',form=form)

@app.route('/pubtrans/')
def pubtrans():
    return render_template('/Fadhilah/Pubtrans.html')

@app.route('/pollutant/')
def pollutant():
    return render_template('/Fadhilah/Pollutant.html')

@app.route('/mrtfeedback/')
def mrtfeedback():
    return render_template('/Bryan/MRTFeedback.html')

@app.route('/mrtstatus/')
def mrtstatus():
    return render_template('/Bryan/MRTStatus.html')

@app.route('/mrtoperatinghours/')
def mrtoperatinghours():
    return render_template('/Bryan/MRTOperatingHours.html')

if __name__ == '__main__':
    app.secret_key = 'secret123'
    app.run(debug=True)
