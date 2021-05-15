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
            printrep = cur.execute('select * from accounts natural join accounttransactions order by date(datetime)')

            if printrep > 0:
                printrepdetail = cur.fetchall()
                return render_template('/admin/printreports.html', printrepdetail=printrepdetail)
            else:
                return "DATA NOT FOUND!!!" 
    
    except:
        return redirect('/admin')
    

@app.route('/admin/printaccounts')
def printaccounts():
    try:
        if logadmin.nim() == "":
            return redirect('/admin')
        else:
            cur = mysql.connection.cursor()

            printrep = cur.execute('select accountid,customerid,type,balance,name from accounts natural join customers')

            if printrep > 0:
                printrepdetail = cur.fetchall()
                return render_template('/admin/printaccounts.html', printrepdetail=printrepdetail)
            else:
                return "DATA NOT FOUND!!!" 
    
    except:
        return redirect('/admin')
    
    
@app.route('/admin/delete/accounts/<int:id>')
def delaccounts(id):
    try:
        if logadmin.nim() == "":
            return redirect('/admin')
        else:

            cur = mysql.connection.cursor()
            cur.execute(f"delete from accounttransactions where accountid='{id}'")
            cur.connection.commit()
            cur.execute(f"delete from accounts where accountid='{id}'")
            cur.connection.commit()
            cur.close()

            return redirect('/admin/printaccounts')
    
    except:
        return redirect('/admin')

@app.route('/admin/printcustomers')
def printcustomer():
    try:
        if logadmin.nim() == "":
            return redirect('/admin')
        else:
            cur = mysql.connection.cursor()
            cur.execute("select customerid,name,address,phone,email from customers")
            printcust = cur.fetchall()
            print(printcust)

            return render_template('/admin/printcustomer.html', printcust=printcust)

    except:
        return redirect('/admin')

@app.route('/admin/delete/customers/<int:id>')
def delcustomers(id):
    try:
        if logadmin.nim() == "":
            return redirect('/admin')
        else:
            try:

                cur = mysql.connection.cursor()
                cur.execute(f"delete from customers where customerid='{id}'")
                cur.connection.commit()
                return redirect('/admin/printcustomers')

            except:

                return f"Customer id = {id} still have active accounts"    

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
