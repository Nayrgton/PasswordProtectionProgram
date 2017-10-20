import peewee

db = peewee.SqliteDatabase('pppDatabase.db')
db.connect()

class Account(peewee.Model):
##    AccID = peewee.FixedCharField(20, null=False, unique=True, )
    UserName = peewee.CharField()
    Password = peewee.CharField()

    class Meta:
        database = db
    
def DeleteTable():
    db.drop_table(Account)
    db.create_table(Account)

def Insert(U,P):
    newAcc = Account(UserName=U,Password=P)
    newAcc.save()
