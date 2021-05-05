from flask import Flask,render_template,request,redirect,url_for
from flask_mysqldb import MySQL
from items import *
from items.userlog import *
from datetime import date
import os

global today
today= date.today()


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
            return redirect('/login')
            
        else:
            return render_template('menu.html', userlog=logdata.name())
    except:
        return redirect('/login')

@app.route('/accounts/register',methods=['GET','POST'])
def createaccount():
    if request.method == 'POST':
        try:
            if logdata.idcust == "":
                return redirect('/login')

            else:
                accid = request.form['accid']
                tipe = request.form['tipe']

                cur = mysql.connection.cursor()
                cur.execute('select accountid from accounts')
                idlist= cur.fetchall()

                for i in range(len(idlist)):
                    if(str(accid) == str(idlist[i][0])):
                        return "ACCOUNTID NOT AVAILABLE, TRY ANOTHER"

                if tipe == "Loan":
                    cur = mysql.connection.cursor()
                    cur.execute(f"insert into accounts values ({accid},'{logdata.idcust()}','{tipe}',{1500000})")
                    cur.connection.commit()
                else:
                    cur = mysql.connection.cursor()
                    cur.execute(f"insert into accounts values ({accid},'{logdata.idcust()}','{tipe}',{0})")
                    cur.connection.commit()

                return redirect(url_for('accounts'))
        except:
            return redirect('/login')
    
    else:
        try:
            if logdata.idcust == "":
                    return redirect('/login')
            else:
                return render_template('accounts/register.html')
        except:
            return redirect('/login')

@app.route('/accounts',methods=['GET','POST'])
def accounts():
    try:
        if logdata.idcust() == "":
            return redirect('/login')
        else:
            cur = mysql.connection.cursor()
            accdata = cur.execute(f"select * from accounts where customerid='{loginid}'")
            
            if accdata > 0:
                accdatadetail = cur.fetchall()
                return render_template('accounts.html', accdatadetail=accdatadetail)

            else:
                return render_template('accounts.html')
    except:
        return redirect('/login')

    return render_template('accounts.html')

@app.route('/accounts/transactions/',methods=['GET','POST'])
def transactions():
    try:
        if logdata.idcust() == "":
            return redirect('/login')
            
        else:
            cur = mysql.connection.cursor()
            transac = cur.execute(f"select * from accounttransactions where accountid in (select accountid from accounts where customerid='{loginid}')")

            if transac > 0:
                transacdetail = cur.fetchall()
                return render_template('/accounts/transactions.html', transacdetail=transacdetail)
            else:
                return render_template('/accounts/transactions.html')
    except:
        return redirect('/login')



@app.route('/accounts/detail/<int:id>', methods=['GET'])
def detail(id):
    global acc
    if logdata.idcust() == "":
        return redirect('/login')
    else:
        cur = mysql.connection.cursor()
        det = cur.execute(f"select * from accounts where accountid='{id}'")
        det = cur.fetchall()


        if str(det[0][2]) == "Saving":
            acc = Saving(det[0][0],det[0][3])
        elif str(det[0][2]) == "Checking Account":
            acc = Checking(det[0][0],det[0][3])
        elif str(det[0][2]) == "Loan":
            acc = Loan(det[0][0],det[0][3])
        

        return render_template('/accounts/detail.html',id=id, det=det, all=acc)

@app.route('/accounts/deposit/<int:id>', methods=['GET','POST'])
def deposit(id):
    if request.method == 'POST':
        try:
            if logdata.idcust() == "":
                return redirect('/login')
            else:
                deps = request.form['amount']
                cur = mysql.connection.cursor()
                dep = cur.execute(f"select balance from accounts where accountid='{id}'")
                dep = cur.fetchall()
                cur.close()

            depo = int(deps)
            acc.deposit(depo)
            
            day = today.strftime("%Y-%m-%d")
            cur = mysql.connection.cursor()
            cur.execute(f"insert into accounttransactions values ({id},'{day}','Deposit','{depo}')")
            cur.connection.commit()

            return redirect('/accounts')
            
        except:
            return redirect('/login')
    else:
        try:
            if logdata.idcust() == "":
                return redirect('/login')
            else:
                cur = mysql.connection.cursor()
                dep = cur.execute(f"select * from accounts where accountid='{id}'")
                dep = cur.fetchall()

                return render_template('/accounts/deposit.html',id=id, dep=dep)
        except:
            return redirect('/login')

@app.route('/accounts/withdraw/<int:id>', methods=['GET','POST'])
def withdraw(id):
    if request.method == 'POST':
        try:
            if logdata.idcust() == "":
                return redirect('/login')
            else:
                wits = request.form['amount']
                cur = mysql.connection.cursor()
                wd = cur.execute(f"select balance from accounts where accountid='{id}'")
                wd = cur.fetchall()
                cur.close()

            wits = int(wits)

            if int(acc.balanceEnquiry() - wits) > 0:
                acc.withdraw(wits)

                day = today.strftime("%Y-%m-%d")
                cur = mysql.connection.cursor()
                cur.execute(f"insert into accounttransactions values ({id},'{day}','Withdraw','{wits}')")
                cur.connection.commit()

                return redirect('/accounts')
            else:
                return "YOUR BALANCE IS INSUFFICIENT"
            
        except:
            return redirect('/login')
    else:
        try:
            if logdata.idcust() == "":
                return redirect('/login')
            else:
                cur = mysql.connection.cursor()
                wd = cur.execute(f"select * from accounts where accountid='{id}'")
                wd = cur.fetchall()

                return render_template('/accounts/withdraw.html',id=id, wd=wd)
        except:
            return redirect('/login')
