import peewee

db = peewee.SqliteDatabase('pppDatabase.db')

class Account(peewee.Model):
    AccID = peewee.FixedCharField(20, unique=True)
    UserName = peewee.CharField()
    Password = peewee.CharField()

    class Meta:
        database = db
        
    
