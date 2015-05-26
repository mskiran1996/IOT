from django.db import models
from masterdata.models import *
from transportation.models import *
from django.contrib.auth.models import User
from django.utils import timezone
import datetime

class Route(Base):
    origin_address = models.CharField(_("Origin Address"), max_length = 100, blank = True, null = True)
    destination_address = models.CharField(_("Destination Address"), max_length = 100, blank = True, null = True)
    
    def __unicode__(self):
        return u"%s" %(self.origin_address)


class Load_Specification(Base):
    line_number = models.CharField(_("Line Number"), max_length = 100)
    type_of_load = models.ForeignKey(Type_of_load, blank=True, null=True)
    dimesions = models.ForeignKey(Dimesions, blank=True, null = True)
    quantity = models.CharField(_("Quantity"), max_length = 100, blank = True, null = True)
    truck_info = models.ForeignKey(Truck_Info, blank=True, null=True)
    
    def __unicode__(self):
        return u"%s" %(self.line_number)


class Insurance_Required(Base):
    short_description = models.CharField(_("Line Number"), max_length = 100, blank = True, null = True)
    value_of_goods = models.CharField(_("Line Number"), max_length = 100, blank = True, null = True)
    
    def __unicode__(self):
        return u"%s" %(self.short_description)


class Special_Instructions(Base):
    flammable = models.CharField(_("Line Number"), max_length = 100)
    vibration_sensitive = models.CharField(_("Line Number"), max_length = 100, blank = True, null = True)
    humidity_sensitive = models.CharField(_("Line Number"), max_length = 100, blank = True, null = True)
    temperature_sensitive = models.CharField(_("Line Number"), max_length = 100, blank = True, null = True)
    locked_load = models.FileField(upload_to="media_files", blank = True, null = True)
    loading = models.CharField(_("Loading Time"), max_length=100, blank=True, null=True)
    unloading = models.CharField(_("Unloading Time"), max_length=100, blank=True, null=True)
    other_manual_services = models.CharField(_("Other Manual Services"), max_length = 100, blank = True, null = True)
    estimated_time = models.CharField(_("Estimated Time"), max_length = 100, blank = True, null = True)
    insurance_required = models.ForeignKey(Insurance_Required)

    def __unicode__(self):
        return u"%s" %(self.flammable)


class Shipment(Base):
    route = models.ForeignKey(Route)
    load_specifications = models.ForeignKey(Load_Specification, blank=True, null=True)
    total_weight = models.CharField(_("Total Weight"), max_length=100, blank = True, null = True)
    special_instrucations = models.ForeignKey(Special_Instructions, blank=True, null=True)
    schedule = models.ForeignKey(Schedule, blank=True, null=True)
    shipment_id_no = models.CharField(_("Shipment Identification NUmber"), max_length=100, blank = True, null = True)
    shipment_doc = models.FileField(upload_to="media_files", blank = True, null = True)
    shipment_location = models.ForeignKey(Location, blank=True, null=True)
    
    def __unicode__(self):
        return u"%s" %(self.total_weight)

Current_Status = (('Accepted','Accepted'),('Rejected','Rejected'))

class Shipment_Details(Base):
    current_status = models.CharField(max_length=40,choices=Current_Status)
    shipment = models.ForeignKey(Shipment)
    truck_details = models.ForeignKey(Trucks)
    rate_truck_driver = models.CharField(_("Rate Truck Driver"), max_length=100, blank = True, null = True)
    rate_customer = models.CharField(_("Rate Customer "), max_length=100, blank = True, null = True)
    
    def __unicode__(self):
        return u"%s" %(self.shipment)
