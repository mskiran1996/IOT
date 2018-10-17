from django.db import models
from shipment.models import *
from django.utils.translation import ugettext_lazy as _


class Customer_Payment(Base):
    shipment = models.OneToOneField(Shipment)
    transaction_status = models.CharField(max_length = 100, blank = True, null = True)
    transaction_type = models.CharField(max_length = 100, blank = True, null = True)
    transaction_id = models.CharField(max_length = 100, blank = True, null = True)
    transaction_date = models.DateTimeField(blank = True, null = True)
    created_by = models.ForeignKey(User)


class Truck_Driver_Payment(Base):
    shipment = models.OneToOneField(Shipment)
    transaction_status = models.CharField(max_length = 100, blank = True, null = True)
    transaction_type = models.CharField(max_length = 100, blank = True, null = True)
    transaction_id = models.CharField(max_length = 100, blank = True, null = True)
    transaction_date = models.DateTimeField(blank = True, null = True)
    created_by = models.ForeignKey(User)



class Refund(Base):
    shipment = models.ForeignKey(Shipment)
    amount = models.DecimalField(max_digits=10, decimal_places=1, blank=True, null=True)
    refund_date = models.DateTimeField()
    refund_type = models.IntegerField(default = 0)
    customer = models.ForeignKey(User_Profile, blank = True, null = True)
    created_by = models.ForeignKey(User)
    refund_status = models.CharField(max_length = 100, blank = True, null = True)
