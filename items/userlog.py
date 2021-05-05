from flask import Flask,render_template,request
from flask_mysqldb import MySQL
from items import *

class Account:
    def __init__ (self,idacc,balance):
        self.__id=idacc
        self.__balance=balance
    
    def deposit(self,depo):
        cur = mysql.connection.cursor()
        cur.execute(f"update accounts set balance={int(self.__balance + depo)} where accountid='{self.__id}'")
        cur.connection.commit()
        cur.close()
        
    def withdraw(self,wits):
        cur = mysql.connection.cursor()
        cur.execute(f"update accounts set balance={int(self.__balance - wits)} where accountid='{self.__id}'")
        cur.connection.commit()
        cur.close()

    def balanceEnquiry(self):
        return self.__balance

class Checking(Account):
    def __init__(self,idcost,balance):
        super().__init__(idcost,balance)

        if balance < 0:
            self.__overdraft = balance
        else:
            self.__overdraft=0

    def __str__(self):
        return (f"This is Checking Account, Overdraft : {self.__overdraft}")

class Saving(Account):
    def __init__(self,idcost,balance):
        super().__init__(idcost,balance)
        self.__interestrate=0.002 * balance

    def __str__(self):
        return (f"This is Saving Account, Interest rate : {self.__interestrate}")

class Loan(Account):
    def __init__(self,idcost,balance):
        super().__init__(idcost,balance)
        self.__principalamount=1500000
        self.__interestrate=0.01 * balance
        self.__loanduration=0

    def __str__(self):
        return (f"This is Loan Account, Interest rate : {self.__interestrate}, Principal Amount : {self.__principalamount}, Loan Duration : {self.__loanduration}")

class Customer:
    def __init__(self,idpengguna,nama,address,phone,email):
        self.__idpengguna=idpengguna
        self.__nama=nama
        self.__address=address
        self.__phone=phone
        self.__email=email
    
    def idcust(self):
        return self.__idpengguna

    def name(self):
        return self.__nama
    
    def __str__(self):
        return f'ID : {self.__idpengguna}\nNama: {self.__nama}\nAddress : {self.__address}\nPhone : {self.__phone}\nEmail : {self.__email}'

    def __del__(self):
        return "Sucessfully Logout"

class Admin:
    def __init__(self,nim,namaAdmin,password):
        self.__nim=nim
        self.__nama=namaAdmin
        self.__password=password

    def nim(self):
        return self.__nim

    def name(self):
        return self.__nama
        
    def __del__(self):
        return "Sucessfully Logout"

