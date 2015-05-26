from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
import datetime

class Base(models.Model):
    active = models.PositiveIntegerField(default = 2)
    created_on = models.DateTimeField(auto_now_add = True)
    modified_on = models.DateTimeField(auto_now = True)
    createdBy = models.ForeignKey(User, blank = True, null = True)
    modifiedBy = models.ForeignKey(User, blank = True, null = True)

    class Meta:
        abstract = True


class Country(Base):
    name = models.CharField(_("Country *"), max_length = 100)

    def __unicode__(self):
        return u"%s" %(self.name)


class State(Base):
    country = models.ForeignKey(Country)
    name = models.CharField(_("State *"), max_length = 100)

    def __unicode__(self):
        return u"%s" %(self.name)


class City(Base):
    state = models.ForeignKey(State)
    name = models.CharField(_("City *"), max_length = 100)

    def __unicode__(self):
        return u"%s" %(self.name)


class Pincode(Base):
    city = models.ForeignKey(State)
    name = models.CharField(_("Pincode *"), max_length = 100)

    def __unicode__(self):
        return u"%s" %(self.name)


class Designation(Base):
    name = models.CharField(_("Designation * "),max_length = 100)

    def __unicode__(self):
        return u"%s" %(self.name)


class Type_of_users(Base):
    name = models.CharField(_("Type of users"), max_length=100)

    def __unicode__(self):
        return u"%s" %(self.name)


class Payment_Type(Base):
    name = models.CharField(_("Payment Type"), max_length=100)

    def __unicode__(self):
        return u"%s" %(self.name)


class Type_of_load(Base):
    name = models.CharField(_("Type of load"), max_length=100)

    def __unicode__(self):
        return u"%s" %(self.name)


class Company_Deparment(Base):
    name = models.CharField(_("Company Deparment"), max_length=100)

    def __unicode__(self):
        return u"%s" %(self.name)


class Truck_Info(Base):
    truck_make = models.CharField(_("Truck Make"), max_length=100, blank = True, null = True)
    truck_model = models.CharField(_("Truck Model"), max_length=100, blank = True, null = True)
    truck_tonnage = models.CharField(_("Truck Tonnage"), max_length=100, blank=True, null = True)
    truck_features = models.CharField(_("Truck Features"), max_length=100, blank=True, null = True)
    temperature_controlled = models.CharField(_("Temperature Controlled"), max_length=100, blank=True, null = True)
    flamable_liquid_carrier = models.BooleanField(default = False)
    closed_contanier = models.BooleanField(default = False)
    closed_with_tarp =models.BooleanField(default = False)
    length = models.CharField(_("Length"), max_length=100) 
    width = models.CharField(_("Width"), max_length=100)
    height = models.CharField(_("Height"), max_length=100)
    truck_description = models.CharField(_("Truck Description"), max_length=100, blank=True, null = True)
    
    def __unicode__(self):
        return u"%s" %(self.truck_model)


class Truck_Driver(Base):
    name = models.CharField(_("Name"), max_length=100, blank = True, null = True)
    address = models.CharField(_("Address"), max_length=100, blank = True, null = True)
    phone_number = models.CharField(_("Phone"), max_length=100, blank = True, null = True)
    dl_number = models.CharField(_("Driving License Number"), max_length=100, blank = True, null = True)
    dl_exp_date = models.CharField(_("License Expiry Date"), max_length=100, blank = True, null = True)
    dl_doc = models.FileField(upload_to="media_files", blank = True, null = True)
    profile_image = models.ImageField(upload_to='static/images',blank=True,null=True)
    
    def __unicode__(self):
        return u"%s" %(self.name)


class Dimesions(Base):
    length = models.CharField(_("Length"), max_length=100) 
    width = models.CharField(_("Width"), max_length=100)
    height = models.CharField(_("Height"), max_length=100)
    
    def __unicode__(self):
        return u"%s" %(self.length)


class Contact_Us(Base):
    type_of_user = models.ForeignKey(Type_of_users)
    company_name = models.CharField(_("Company Name"), max_length=100)
    contact_person = models.CharField(_("Contact Person"), max_length=100)
    designation = models.ForeignKey(Designation)
    contact_number = models.CharField(_("Contact Number"), max_length=100)
    email = models.EmailField(_("Email"), max_length = 100)
    address = models.CharField(_("Address"), max_length = 100, blank = True, null = True)
    message = models.CharField(_("Message"), max_length = 100, blank = True, null = True)
    
    def __unicode__(self):
        return u"%s" %(self.company_name)


Request_Status = (('New','New'),('Open','Open'),('Closed - Not Interested','Closed - Not Interested'),('Closed - Interested to Reg','Closed - Interested to Reg'),('Closed - Registered','Closed - Registered'))


class Track_Contact_Us(Base):
    contact_us = models.ForeignKey(Contact_Us)
    request_status = models.CharField(max_length=40,choices=Request_Status)
    resason = models.CharField(_("Reason"), max_length = 100, blank = True, null = True)
    notes = models.CharField(_("Notes"), max_length = 100, blank = True, null = True)
    assigned_user = models.ForeignKey(User, blank = True, null = True)
    
    def __unicode__(self):
        return u"%s" %(self.contact_us__company_name)


class Schedule(Base):
    schedule_type = models.CharField(_("Schedule Type"), max_length = 100, blank = True, null = True)
    pick_up = models.DateTimeField(auto_now_add = True)
    pickup_cutoff = models.CharField(_("Pickup Cutoff"), max_length = 100)
    delivery = models.CharField(_("Delivery"), max_length = 100)
    delivery_cutoff = models.CharField(_("Delivery Cutoff"), max_length = 100)
    
    def __unicode__(self):
        return u"%s" %(self.schedule_type)
