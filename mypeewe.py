import pandas
from peewee import *
db=SqliteDatabase('companydetail.db')

class Company(Model):

    Company_Name = CharField(null = True)
    Type_of_Company=CharField()
    Whatsapp_Number=CharField(null = True)
    Fax=CharField(null = True)
    Linkedin_Profile=CharField(null = True)
    Presence_in_India=CharField(null = True)

    class Meta:
        database=db

    def __str__(self):
        return self.Company_Name

class Website(Model):

    Web_owner=ForeignKeyField(Company)
    Web_address = CharField()

    class Meta:
        database = db


class Phone(Model):
    Phone_owner = ForeignKeyField(Company)
    Phone_number = CharField()

    class Meta:
        database = db



class Email(Model):
    Email_owner = ForeignKeyField(Company)
    Email_address = CharField()

    class Meta:
        database = db


class Address(Model):
    Address_owner = ForeignKeyField(Company)
    Address_location = CharField()

    class Meta:
        database = db

def create_tables():
    with db:
        db.create_tables([Company, Website, Phone,Email,Address])



create_tables()