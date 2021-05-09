from flask import Flask,render_template,request
from flask_mysqldb import MySQL
from items import *
from items.userlog import *
from items.admin import *
from items.customer import *


@app.route('/',methods=['GET','POST'])
def index():
    return render_template('index.html')

@app.route('/aboutus')
def aboutus():
    return render_template('aboutus.html')