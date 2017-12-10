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
def mrtTiming():
    return render_template('mrtTiming.html')

@app.route('/my-link/')
def my_link():
    print('I got clicked!')
    return 'Click.'

@app.route('/at/')
def at():
    return render_template('alternative_transport.html')

@app.route('/mc')
def mc():
    return render_template('MrtCrowded.html')

if __name__ == '__main__':
    app.secret_key = 'secret123'
    app.run()


