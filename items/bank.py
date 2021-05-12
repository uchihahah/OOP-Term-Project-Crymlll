from flask import Flask,render_template,request,redirect
from flask_mysqldb import MySQL
from items import *
from items.userlog import *
from datetime import date


global today
today= date.today()

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