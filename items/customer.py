from flask import Flask,render_template,request,redirect,url_for
from flask_mysqldb import MySQL
from items import *
from items.userlog import *


@app.route('/login',methods=['GET','POST'])
def login():
    global logdata
    global loginid
    
    if request.method == 'POST':
        customer_id = request.form['ID']
        name = request.form['name']

        cur = mysql.connection.cursor()
        
        cur.execute("select customerid from customers")
        checkid= cur.fetchall()
        cur.execute("select name from customers")
        checkname= cur.fetchall()
        cur.close()

        for i in range(len(checkid)):
            if str(customer_id) == str(checkid[i][0]) and str(name) == str(checkname[i][0]):
                cur = mysql.connection.cursor()
                cur.execute(f"select * from customers where customerid='{customer_id}'")
                logon= cur.fetchall()
                cur.close()

                loginid= customer_id
                logdata = Customer(logon[0][0],logon[0][1],logon[0][2],logon[0][3],logon[0][4])
                print(logdata.__dict__)

                return redirect(url_for('menu'))
                        
        
    return render_template('login.html')

@app.route('/menu')
def menu():
    try:
        if logdata.idcust() == "":
            return "LOGIN FIRST BEFORE CONTINUE"
            
        else:
            return render_template('menu.html')
    except:
        return "LOGIN FIRST BEFORE CONTINUE"

@app.route('/accounts',methods=['GET','POST'])
def accounts():
    try:
        if logdata.idcust() == "":
            return "LOGIN FIRST BEFORE CONTINUE"
        else:
            cur = mysql.connection.cursor()
            accdata = cur.execute(f"select * from accounts where customerid='{loginid}'")
            userlog=logdata.name()
            
            if accdata > 0:
                accdatadetail = cur.fetchall()
                return render_template('accounts.html', accdatadetail=accdatadetail, userlog=userlog)

            else:
                return "NO DATA ACCOUNT!"
    except:
        return "LOGIN FIRST BEFORE CONTINUE"

    return render_template('accounts.html')

@app.route('/transactions',methods=['GET','POST'])
def transactions():
    try:
        if logdata.idcust() == "":
            return "LOGIN FIRST BEFORE CONTINUE"
            
        else:
            cur = mysql.connection.cursor()
            transac = cur.execute(f"select * from accounttransactions where accountid in (select accountid from accounts where customerid='{loginid}')")

            if transac > 0:
                transacdetail = cur.fetchall()
                return render_template('transactions.html', transacdetail=transacdetail)
            else:
                return "TIDAK ADA DATA!!!!"
    except:
        return "LOGIN FIRST BEFORE CONTINUE"


@app.route('/accounts/detail/<int:id>', methods=['GET'])
def detail(id):
    if logdata.idcust() == "":
        return "LOGIN FIRST"
    else:
        cur = mysql.connection.cursor()
        det = cur.execute(f"select * from accounts where accountid='{id}'")
        det = cur.fetchall()

        return render_template('/accounts/detail.html',id=id, det=det)

