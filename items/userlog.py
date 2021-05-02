from flask import Flask,render_template,request
from flask_mysqldb import MySQL


class Account:
    def __init__ (self,idcost,balance):
        self.__id=idcost
        self.__balance=balance
    
    def deposit(self):
        pass

    def withdraw(self):
        pass

    def balanceEnquiry(self):
        pass

class Checking(Account):
    def __init__(self,idcost,balance):
        super().__init__(idcost,balance)
        self._overdraft=0

class Saving(Account):
    def __init__(self,idcost,balance):
        super().__init__(idcost,balance)
        self._interestrate=0.002 * balance

class Loan(Account):
    def __init__(self,idcost,balance):
        super().__init__(idcost,balance)
        self._principalamount=0
        self._interestrate=0
        self._loanduration=0

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

class Admin:
    def __init__(self,nim,namaAdmin,password):
        self.__nim=nim
        self.__nama=namaAdmin
        self.__password=password

    def nim(self):
        return self.__nim
    def name(self):
        return self.__nama

