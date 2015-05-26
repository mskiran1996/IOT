from django.db import models
from masterdata.models import *
from django.contrib.auth.models import User
from django.utils import timezone
import datetime

Registration_Status = (('Rejected','Rejected'),('Saved','Saved'),('Blocked','Blocked'))


class Transportation_Company(Base):
    company_name = models.CharField(_("Company Name"), max_length=100)
    company_reg_off_address = models.CharField(_("Company Registered Office Address"), max_length=100, blank = True, null = True)
    contact_person = models.CharField(_("Contact Person"), max_length=100, blank = True, null = True)
    mobile_number = models.CharField(_("Mobile"), max_length=100, blank = True, null = True)
    landline_number2 = models.CharField(_("Landline"), max_length=100, blank = True, null = True)
    address = models.CharField(_("Address"), max_length=100, blank = True, null = True)
    designation = models.ForeignKey(Designation, blank = True, null = True)
    company_deparment = models.ForeignKey(Company_Deparment, blank = True, null = True)
    company_license_number = models.CharField(_("Company License Number"), max_length=100, blank = True, null = True)
    company_verification_doc = models.FileField(upload_to="media_files", blank = True, null = True)
    company_verification_remarks = models.CharField(_("Company Verification Remarks"), max_length=100, blank = True, null = True)
    company_verification_by = models.ForeignKey(User, blank = True, null = True)
    payment_type = models.ForeignKey(Payment_Type, blank = True, null = True)
    user = models.ForeignKey(User)
    user_email = models.EmailField(_("User Email"), max_length = 100)
    user_phone_number = models.CharField(_("User Mobile"), max_length=100, blank = True, null = True)
    user_address = models.CharField(_("User Address"), max_length=100, blank = True, null = True)
    status = models.CharField(max_length=40,choices=Registration_Status)
    
    
    def __unicode__(self):
        return u"%s" %(self.company_name)


class Commercial_User(Base):
    customer_company_name = models.CharField(_("Customer Company Name"), max_length=100)
    company_reg_off_address = models.CharField(_("Company Registered Office Address"), max_length=100, blank = True, null = True)
    contact_person = models.CharField(_("Contact Person"), max_length=100, blank = True, null = True)
    mobile_number = models.CharField(_("Mobile"), max_length=100, blank = True, null = True)
    landline_number2 = models.CharField(_("Landline"), max_length=100, blank = True, null = True)
    address = models.CharField(_("Address"), max_length=100, blank = True, null = True)
    designation = models.ForeignKey(Designation, blank = True, null = True)
    company_license_number = models.CharField(_("Company License Number"), max_length=100, blank = True, null = True)
    company_verification_doc = models.FileField(upload_to="media_files", blank = True, null = True)
    company_verification_remarks = models.CharField(_("Company Verification Remarks"), max_length=100, blank = True, null = True)
    company_verification_by = models.ForeignKey(User, blank = True, null = True)
    payment_type = models.ForeignKey(Payment_Type, blank = True, null = True)
    user = models.ForeignKey(User)
    user_email = models.EmailField(_("User Email"), max_length = 100)
    user_phone_number = models.CharField(_("User Mobile"), max_length=100, blank = True, null = True)
    user_address = models.CharField(_("User Address"), max_length=100, blank = True, null = True)
    status = models.CharField(max_length=40,choices=Registration_Status)
    
    def __unicode__(self):
        return u"%s" %(self.company_name)


class Sub_Accounts(Base):
    company_deparment = models.ForeignKey(Company_Deparment, blank = True, null = True)
    address = models.CharField(_("Address"), max_length=100, blank = True, null = True)
    phone_number = models.CharField(_("Phone"), max_length=100, blank = True, null = True)
    contact_person = models.CharField(_("Contact Person"), max_length=100, blank = True, null = True)
    designation = models.ForeignKey(Designation, blank = True, null = True)
    email = models.EmailField(_("Email Id of Contact Person"), max_length = 100)
    user = models.ForeignKey(User)
    
    def __unicode__(self):
        return u"%s" %(self.company_deparment__name)


class Trucks(Base):
    truck_reg_no = models.CharField(_("Truck Registration Number"), max_length=100, blank = True, null = True)
    truck_info = models.ForeignKey(Truck_Info, blank = True, null = True) 
    truck_doc = models.FileField(upload_to="media_files", blank = True, null = True)
    truck_insurance = models.CharField(_("Truck Insurance"), max_length=100, blank=True, null = True)
    truck_permit_information = models.CharField(_("Truck Permit"), max_length=100, blank=True, null = True)
    truck_driver = models.ForeignKey(Truck_Driver, blank=True, null=True)
    unique_key = models.CharField(_("Unique Key"), max_length=100, blank=True, null = True)
    anroid_device_id = models.CharField(_("Anroid Device Id"), max_length=100, blank=True, null = True)
    
    
    def __unicode__(self):
        return u"%s" %(self.truck_reg_no)



class Locations(Base):
    name_of_location = models.CharField(_("Name of Location"), max_length=100)
    address1 = models.CharField(_("Address1"), max_length=100, blank=True, null = True)
    address2 = models.CharField(_("Address2"), max_length=100, blank=True, null = True)
    country = models.ForeignKey(Country, blank=True, null=True)
    state = models.ForeignKey(State, blank=True, null=True)
    city = models.ForeignKey(City, blank=True, null=True)
    pin_code = models.ForeignKey(Pincode, blank=True, null=True)
    latitude = models.CharField(_("Latitude"), max_length=200, blank=True, null=True)
    longitude = models.CharField(_("Longitude"), max_length=200, blank=True, null=True)
    
    def __unicode__(self):
        return u"%s" %(self.name__of_location)


class Load_Types(Base):
    type_of_load = models.ForeignKey(Type_of_load)
    name = models.CharField(_("Name"), max_length=100, blank=True, null = True)
    description = models.CharField(_("Description"), max_length=100, blank=True, null = True)
    dimesions = models.ForeignKey(Dimesions, blank=True, null=True)
    unit = models.CharField(_("Unit"), max_length=100, blank=True, null = True)
    truck_type = models.ForeignKey(Truck_Info, blank=True, null=True)
    stackable = models.BooleanField(default = True)
    
    def __unicode__(self):
        return u"%s" %(self.name)

