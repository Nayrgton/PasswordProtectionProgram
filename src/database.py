## @file database.py
#  @title PPP_database
#  @author Joseph Lu, luy89
#  @date 20/10/2017 

import peewee

db = peewee.SqliteDatabase('pppDatabase.db')
db.connect()

## @brief SQLite table to store passwords
#  @detail Use peewee orm library to create a table class that stores accounts
class Account(peewee.Model):
##    AccID = peewee.FixedCharField(20, null=False, unique=True)
    AccName = peewee.CharField()
    UserName = peewee.CharField()
    Password = peewee.CharField()

    class Meta:
        database = db

## @brief Instantiate new empty table
def ResetTable():
    db.drop_table(Account)
    db.create_table(Account)

## @brief Insert new Username/Password
#  @param U username
#  @param P password
def Insert(U, P):
    Account(UserName=U, Password=P).save()

## @brief Get Table Row with Account Name
#  @param name Account Name
def GetU(name):
    return Account.get(Account.AccName == name)
