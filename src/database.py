## @file database.py
#  @title PPP_database
#  @author Joseph Lu, luy89
#  @date 20/10/2017 

import peewee

#  database connection db
db = peewee.SqliteDatabase('pppDatabase.db')
db.connect()

## @brief Base Model for database connection
#  @detail All other Tables will connect automatically to our database
class BaseModel(peewee.Model):
    class Meta:
        database = db

## @brief SQLite table to store passwords
#  @detail Use peewee orm library to create a table class that stores accounts
#  @param AccID Account ID and Primary Key
#  @param AccType Type of Account used
#  @param UserName Account Username
class Account(BaseModel):
    AccID = peewee.PrimaryKeyField()
    AccType = peewee.CharField()
    UserName = peewee.CharField()

## @brief SQLite table to store hash keys and hash values
#  @detail use peewee orm library to create a table class that stores hash values and hash keys in a database. This table is not accessabile via the application. 
#  @param Eid Encrypted Password ID and Foreign key from Account ID
#  @param HashVal Hashed value of Password
#  @param HashKey Key to Decrypt Password
class Encrypt(BaseModel):
    Eid = peewee.ForeignKeyField(Account, on_field='AccID', primary_key=True, on_delete='CASCADE')
    HashVal = peewee.CharField(True, unique=True)
    HashKey = peewee.FixedCharField()

## @brief Instantiate new empty table
def ResetTable():
    db.drop_table(Account)
    db.create_table(Account)

## @brief Insert new Username/Password
#  @param T Account Type
#  @param U username
#  @param Hv Hash Value
#  @param Hk Hash Key
def Insert(T, U, Hv, Hk):
    Account(AccType=T, UserName=U).save()
    Encrypt(HashVal=Hv, HashKey=Hk).save()

## @brief Get Table Rows with Account Name
#  @param type Account type
def GetA(Atype):
    return Account.select(Account.AccType == Atype)

## @brief Get Table Row with Username
#  @param name Account Name
def GetU(name):
    return Account.select(Account.UserName == name)

## @brief Delete Table Row with ID
#  @param Aid Account ID
def Delete(Aid):
    Account.delete().where(Account.AccID == Aid).execute()

## @brief Update Table Row with ID
#  @param Aid Account Id and Encrypted ID
#  @param U new Username
#  @param Hv new Hash Value
def Update(Aid, U, Hv):
    Account.update(UserName=U).where(Account.Aid == Aid).execute()
    Encrypt.update(HashVal=Hv).where(Encrypt.Eid == Aid).execute()