from flask import Flask, render_template

import firebase_admin
from firebase_admin import credentials, db

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

@app.route('/routes/')
def routes():
    return render_template('MRT_Routes.html')

@app.route('/my-link/')
def my_link():
  print('I got clicked!')

  return 'Click.'

if __name__ == '__main__':
    app.secret_key = 'secret123'
    app.run()


