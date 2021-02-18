import pandas as pd
from mypeewe import *
# company name shoud not repete
def Create_company():

    data=pd.read_excel('company_details_exel.xls')
    for i in range(len(data)):
        Company_Name = data.iloc[i]['Company Name']
        Type_of_Company=data.iloc[i]['Type of Company']
        Whatsapp_Number=data.iloc[i]['Whatsapp Number']
        Fax=data.iloc[i][' Fax']
        Linkedin_Profile=data.iloc[i]['Linkedin Profile']
        Presence_in_India=data.iloc[i]['Presence in India']
        if Company.select().exists():
            if Company.filter(Company.Company_Name == Company_Name):
                print("exist")
                return
            else:
                company = Company.create(Company_Name=Company_Name, Type_of_Company=Type_of_Company,
                                         Whatsapp_Number=Whatsapp_Number, Fax=Fax, Linkedin_Profile=Linkedin_Profile,
                                         Presence_in_India=Presence_in_India)

        else:
            company=Company.create(Company_Name=Company_Name,Type_of_Company=Type_of_Company,Whatsapp_Number=Whatsapp_Number,Fax=Fax,Linkedin_Profile=Linkedin_Profile,Presence_in_India=Presence_in_India)

        Phone_num=str(data.iloc[i]['Phone Number'])
        if Phone.select().where(Phone.Phone_number==Phone_num).exists() | pd.isna(Phone_num):
            pass
        elif  Phone_num.find('/') == -1:
            phone = Phone.create(Phone_number=Phone_num, Phone_owner=company)
        else:
            print(Phone_num)
            ph_list=Phone_num.split('/')
            res = []
            for h in ph_list:
                res.append(h.replace('\n', ''))
            uniq_list = pd.unique(res)
            print(uniq_list)
            for k in range(len(uniq_list)):
                phone = Phone.create(Phone_number=uniq_list[k], Phone_owner=company)

        Web_address=data.iloc[i]['Website']
        if Website.select().where(Website.Web_address==Web_address).exists() | pd.isna(Web_address):
            pass
        elif  Web_address.find('|') == -1:
            web = Website.create(Web_address=Web_address, Web_owner=company)
        else:
            web_list=Web_address.split('|')
            print(web_list)
            uniq_list1=pd.unique(web_list)
            print(uniq_list1)
            for k in range(len(uniq_list1)):
                web = Website.create(Web_address=uniq_list1[k], Web_owner=company)

        Email_address = data.iloc[i]['Mail']
        if Email.select().where(Email.Email_address==Email_address).exists() | pd.isna(Email_address):
            pass
        elif  Email_address.find('|') == -1:
            mail = Email.create(Email_address=Email_address, Email_owner=company)
        else:
            email_list=Email_address.split('|')
            uniq_list2=pd.unique(email_list)
            for k in range(len(uniq_list2)):
                mail = Email.create(Email_address=uniq_list2[k], Email_owner=company)

        Address_location = data.iloc[i]['Address']
        if Address.select().where(Address.Address_location==Address_location).exists() | pd.isna(Address):
            pass
        elif  Address_location.find('/') == -1:
            address = Address.create(Address_location=Address_location, Address_owner=company)
        else:
            address_list=Address_location.split('/')
            uniq_list3=pd.unique(address_list)
            for k in range(len(uniq_list3)):
                address = Address.create(Address_location=uniq_list3[k], Address_owner=company)


if __name__=='__main__':
    Create_company()
