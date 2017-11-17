## @file database.py
#  @title PPP_database
#  @author Joseph Lu, luy89
#  @date 20/10/2017 

import peewee

#  database connection db
db = peewee.SqliteDatabase('pppDatabase.db')
db.connect()

## @brief Base Model for database connection
#  @details All other Tables will connect automatically to our database
class BaseModel(peewee.Model):
    class Meta:
        database = db

## @brief SQLite table to store passwords
#  @details Use peewee orm library to create a table class that stores accounts
#  @param AccID Account ID and Primary Key
#  @param AccType Type of Account used
#  @param UserName Account Username
class Account(BaseModel):
    ID = peewee.PrimaryKeyField()
    AccName = peewee.CharField(unique=True)
    AccType = peewee.CharField()
    UserName = peewee.CharField(null=True)

## @brief SQLite table to store hash keys and hash values
#  @details use peewee orm library to create a table class that stores hash values and hash keys in a database. This table is not accessabile via the application. 
#  @param Eid Encrypted Password ID and Foreign key from Account ID
#  @param HashVal Hashed value of Password
#  @param HashKey Key to Decrypt Password
class Encrypt(BaseModel):
    ID = peewee.ForeignKeyField(Account, to_field='ID', primary_key=True, on_delete='CASCADE')
    HashVal = peewee.CharField()
    HashKey = peewee.FixedCharField(10)

## @brief Instantiate new empty tables
#  @details Encrypt Table should also be reset when Account is reset
def CreateTables():
    db.create_tables([Account, Encrypt], safe=True)

## @brief Delete tables
#  @details Encrypt Table should also be reset when Account is reset
def DropTables():
    db.drop_tables([Account, Encrypt], safe=True)

## @brief Insert new Account Instance and Encrypt Instance
#  @param N Account Name
#  @param T Account Type
#  @param U username
#  @param Hv Hash Value
#  @param Hk Hash Key
def Insert(Id, N, T, U, Hv, Hk):
    Account.create(ID = Id, AccName=N, AccType=T, UserName=U)
    Encrypt.create(ID=Id, HashVal=Hv, HashKey=Hk)

## @brief search tables with AccId
#  @param Id Account Id
def GetId(id_):
    return (Account
            .select(Account, Encrypt)
            .join(Encrypt)
            .order_by(Account.ID)
            .where(id_==Account.ID)
<<<<<<< HEAD
            .naive()[0]
            )
=======
            .naive()
            )[0]
>>>>>>> Database

## @brief Get Table Rows with Account Type
#  @param Atype Account type
def GetT(Atype):
    return (Account
            .select()
            .join(Encrypt)
            .order_by(Account.ID)
            .where(Account.AccType == Atype)
            .naive()
            )

## @brief Get Table Row with Account name
#  @param Aname Account Name
def GetN(Aname):
    return (Account
            .select()
            .join(Encrypt)
            .order_by(Account.ID)
            .where(Account.AccName == Aname)
            .naive()
            )

## @brief Delete Table Row with ID
#  @param id Account ID
def Delete(id_):
    Account.delete().where(Account.ID == id_).execute()
    Encrypt.delete().where(Encrypt.ID == id_).execute()

## @brief Update Table Row with ID
#  @param Aid Account Id
#  @param U new Username
#  @param Hv new Hash Value
def UpdateU(Aid, U):
    Account.update(UserName=U).where(Account.ID == Aid).execute()

## @brief Update Password with ID
#  @param Aid Account Id (Encrypted ID)
#  @param Hv new Hash Value
def UpdateP(Aid, Hv):
    Encrypt.update(HashVal=Hv).where(Encrypt.ID == Aid).execute()

DropTables();CreateTables()
