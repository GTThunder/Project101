from flask import Flask, render_template,request,redirect,url_for
from firebase import firebase
import firebase_admin
from firebase_admin import credentials, db
from wtforms import SelectField,validators,Form
import numpy as np
from pandas import DataFrame
import matplotlib.pyplot as plt

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/pubtrans/')
def pubtrans():
    return render_template('../templates/Fadhilah/pubTrans.html')