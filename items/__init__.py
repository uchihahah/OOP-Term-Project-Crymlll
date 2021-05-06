from flask import Flask,render_template,request

from flask_mysqldb import MySQL


app = Flask(__name__)

app.config['MYSQL_HOST'] = "sql6.freesqldatabase.com"
app.config['MYSQL_USER'] = "sql6410595"
app.config['MYSQL_PASSWORD'] = "8SqrZ9TiJq"
app.config['MYSQL_DB'] = "sql6410595"

mysql = MySQL(app)

from items import main