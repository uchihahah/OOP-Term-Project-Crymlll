from flask import Flask,render_template,request
from flask_mysqldb import MySQL
from items import *
from items.userlog import *

@app.route('/admin',methods=['GET','POST'])
def admin():
    global logadmin
    if request.method == 'POST':
        admin_id = request.form['ID']
        password = request.form['name']

        cur = mysql.connection.cursor()

        cur.execute('select nim from admin')
        checknim= cur.fetchall()
        cur.execute('select password from admin')
        checkpass= cur.fetchall()
        cur.close()

        for i in range(len(checknim)):
            if str(admin_id) == str(checknim[i][0]) and str(password) == str(checkpass[i][0]):
                cur = mysql.connection.cursor()
                cur.execute(f"select * from admin where nim='{admin_id}'")
                la= cur.fetchall()
                cur.close()

                logadmin=Admin(la[0][0],la[0][1],la[0][2])
                print(logadmin.__dict__)

                return render_template('menuadmin.html')
        
    return render_template('admin.html')

@app.route('/menuadmin',methods=['GET','POST'])
def menuadmin():
    try:
        if logadmin.nim() =="":
            return "Sorry, you must login first"
        else:
            return render_template('menuadmin.html')
    except:
        return "Sorry, you must login first"


@app.route('/regcustomer',methods=['GET','POST'])
def regcustomer():
    if request.method == 'POST':
        try:
            if logadmin.nim() == "":
                return "Sorry, you must login first"
            else:
                customer_id = request.form['ID']
                name = request.form['name']
                address = request.form['address']
                phone = request.form['phone']
                email = request.form['email']

                cur = mysql.connection.cursor()

                cur.execute("INSERT INTO customers (customerid,name,address,phone,email) VALUES (%s,%s,%s,%s,%s)", (customer_id,name,address,phone,email))
                mysql.connection.commit()

                cur.close()

                return "BERHASIL"
        except:
            return "You must login first"

    elif request.method == 'GET':
        try:
            if logadmin.nim() == "":
                return "Sorry, you must login first"
            else:
                return render_template('regcustomer.html')
        except:
            return "Sorry, you must login first"
        
    return render_template('regcustomer.html')

@app.route('/printreports')
def printreport():
    try:
        if logadmin.nim() == "":
            return "You must login first"

        else:
            cur = mysql.connection.cursor()
            printrep = cur.execute('select * from accounttransactions')

            if printrep > 0:
                printrepdetail = cur.fetchall()
                return render_template('printreports.html', printrepdetail=printrepdetail)
            else:
                return "TIDAK ADA DATA!!!" 
    
    except:
        return "You must login first"
    
    return render_template('printreports')