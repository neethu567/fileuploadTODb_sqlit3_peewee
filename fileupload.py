# import sqlalchemy
# from sqlalchemy import create_engine
# from sqlalchemy.ext.declarative import declarative_base
#
# engine=create_engine('sqlite:///memory:',echo=True)
# Base=declarative_base()
#
# from sqlalchemy import  Column,INTEGER,String
#
# class Company(Base):
#
#     __tablename__='Company'
#     id=Column(INTEGER,primary_key=True)
#     Company_Name=Column(String)
#     Type_of_Company=Column(String)
#     Whatsapp_Number=Column(String)
#     Fax=Column(String)
#     Linkedin_Profile=Column(String)
#     Presence_in_India=Column(String)
#
#     def __repr__(self):
#         return "<Company(Company_Name='%s',Linkedin_Profile='%s')>"%(self.Company_Name,self.Linkedin_Profile)

