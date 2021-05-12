from re import I
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
            return "Sorry, you must login first"
        else:
            return render_template('/admin/menu.html')
    except:
        return "Sorry, you must login first"


@app.route('/admin/regcustomer',methods=['GET','POST'])
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
                return render_template('/admin/regcustomer.html')
        except:
            return "Sorry, you must login first"
        

@app.route('/admin/printreports')
def printreport():
    try:
        if logadmin.nim() == "":
            return "You must login first"

        else:
            cur = mysql.connection.cursor()
            printrep = cur.execute('select * from accounts natural join accounttransactions')

            if printrep > 0:
                printrepdetail = cur.fetchall()
                return render_template('/admin/printreports.html', printrepdetail=printrepdetail)
            else:
                return "TIDAK ADA DATA!!!" 
    
    except:
        return "You must login first"
    

@app.route('/admin/printcustomer')
def printcustomer():
    cur = mysql.connection.cursor()

    printrep = cur.execute('select accountid,customerid,type,balance,name from accounts natural join customers')

    if printrep > 0:
        printrepdetail = cur.fetchall()
        return render_template('/admin/printcustomer.html', printrepdetail=printrepdetail)
    else:
        return "TIDAK ADA DATA!!!" 
    
    
@app.route('/admin/delete/customer/<int:id>')
def delcustomer(id):
    cur = mysql.connection.cursor()
    cur.execute(f"delete from accounttransactions where accountid='{id}'")
    cur.connection.commit()
    cur.execute(f"delete from accounts where accountid='{id}'")
    cur.connection.commit()
    cur.close()

    return redirect('/admin/printcustomer')


@app.route('/scheduler')
def scheduler():
    global accttl
    cur = mysql.connection.cursor()
    cur.execute("select * from accounts")
    accttl=cur.fetchall()
    print(accttl)
    
    i=0

    while i in range(len(accttl)):
        print(i)
        if accttl[i][2] == "Loan":
            accloan(i)

        elif accttl[i][2] == "Saving":
            accsaving(i)

        i+=1

    return redirect('/')

def accloan(i):

    cur = mysql.connection.cursor()
    det = cur.execute(f"select * from accounts where accountid='{accttl[i][0]}'")
    det = cur.fetchall()

    cur.execute(f"select count(accountid) from accounttransactions where accountid='{accttl[i][0]}'")
    count = cur.fetchall()
    cnt=count[0][0]/2

    
    cur.execute(f"select amount from accounttransactions where accountid='{accttl[i][0]}'")
    ttl=cur.fetchall()
    
    total=[]
    for j in range(len(ttl)):
        total.append(ttl[j][0])
    
    Sum = sum(total)

    acc = Loan(det[0][0],det[0][3],cnt,Sum)

    payments = (acc.balanceEnquiry()/acc.loanduration())

    if int(acc.balanceEnquiry() - payments) > 0:
        acc.withdraw(payments)

        day = today.strftime("%Y-%m-%d")
        cur = mysql.connection.cursor()
        print(accttl)
        cur.execute(f"insert into accounttransactions values ({accttl[i][0]},'{day}','Pay Loan','{payments}')")
        cur.connection.commit()
        cur.execute(f"insert into accounttransactions values ({accttl[i][0]},'{day}','Interest','{acc.Interest()}')")
        cur.connection.commit()

        return redirect('/accounts')
        
    elif int(acc.balanceEnquiry() - payments) == 0:
        acc.withdraw(payments)

        day = today.strftime("%Y-%m-%d")
        cur = mysql.connection.cursor()
        cur.execute(f"delete from accounttransactions where accountid='{accttl[i][0]}'")
        cur.connection.commit()
        cur.execute(f"delete from accounts where accountid='{accttl[i][0]}'")
        cur.connection.commit()
        cur.close()

def accsaving(i):
    cur = mysql.connection.cursor()
    det = cur.execute(f"select * from accounts where accountid='{accttl[i][0]}'")
    det = cur.fetchall()

    acc = Saving(det[0][0],det[0][3])

    cur.execute(f"update accounts set balance={acc.balanceEnquiry() + acc.Interest()} where accountid='{accttl[i][0]}'")
    cur.connection.commit()
    day = today.strftime("%Y-%m-%d")
    cur.execute(f"insert into accounttransactions values ({accttl[i][0]},'{day}','Interest','{acc.Interest()}')")
    print(det)


    return redirect('/')


