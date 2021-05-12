from flask import Flask,render_template,request,redirect
from flask_mysqldb import MySQL
from items import *
from items.userlog import *
from datetime import date


global today
today= date.today()

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

                return redirect('/admin/menu')
        
    return render_template('/admin.html')

@app.route('/admin/menu',methods=['GET','POST'])
def menuadmin():
    try:
        if logadmin.nim() =="":
            return redirect('/admin')
        else:
            return render_template('/admin/menu.html')
    except:
        return redirect('/admin')


@app.route('/admin/regcustomer',methods=['GET','POST'])
def regcustomer():
    if request.method == 'POST':
        try:
            if logadmin.nim() == "":
                return redirect('/admin')
            else:
                customer_id = request.form['ID']
                name = request.form['name']
                address = request.form['address']
                notelp = request.form['notelp']
                email = request.form['email']
                password = request.form['password']

                cur = mysql.connection.cursor()

                print(name)
                print(notelp)
                print(address)
                print(email)
                print(password)

                cur.execute(f"insert into customers values ('{customer_id}','{name}','{address}','{notelp}','{email}','{password}')")
                mysql.connection.commit()

                cur.close()

                return redirect('/admin/regcustomer')
        except:
            return redirect('/admin')

    elif request.method == 'GET':
        try:
            if logadmin.nim() == "":
                return redirect('/admin')
            else:
                return render_template('/admin/regcustomer.html')
        except:
            return redirect('/admin')
        

@app.route('/admin/printreports')
def printreport():
    try:
        if logadmin.nim() == "":
            return redirect('/admin')

        else:
            cur = mysql.connection.cursor()
            printrep = cur.execute('select * from accounts natural join accounttransactions')

            if printrep > 0:
                printrepdetail = cur.fetchall()
                return render_template('/admin/printreports.html', printrepdetail=printrepdetail)
            else:
                return "DATA NOT FOUND!!!" 
    
    except:
        return redirect('/admin')
    

@app.route('/admin/printcustomer')
def printcustomer():
    try:

        cur = mysql.connection.cursor()

        printrep = cur.execute('select accountid,customerid,type,balance,name from accounts natural join customers')

        if printrep > 0:
            printrepdetail = cur.fetchall()
            return render_template('/admin/printcustomer.html', printrepdetail=printrepdetail)
        else:
            return "DATA NOT FOUND!!!" 
    
    except:
        return redirect('/admin')
    
    
@app.route('/admin/delete/customer/<int:id>')
def delcustomer(id):
    try:

        cur = mysql.connection.cursor()
        cur.execute(f"delete from accounttransactions where accountid='{id}'")
        cur.connection.commit()
        cur.execute(f"delete from accounts where accountid='{id}'")
        cur.connection.commit()
        cur.close()

        return redirect('/admin/printcustomer')
    
    except:
        return redirect('/admin')


@app.route('/logoutadmin')
def logoutadmin():
    global logadmin
    try:
        del logadmin
        return redirect('/')
    except:
        return redirect('/')
