# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('shipment', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer_Payment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('active', models.PositiveIntegerField(default=2)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('modified_on', models.DateTimeField(auto_now=True)),
                ('transaction_status', models.CharField(max_length=100, null=True, blank=True)),
                ('transaction_type', models.CharField(max_length=100, null=True, blank=True)),
                ('transaction_id', models.CharField(max_length=100, null=True, blank=True)),
                ('transaction_date', models.DateTimeField(null=True, blank=True)),
                ('created_by', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
                ('shipment', models.OneToOneField(to='shipment.Shipment')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Refund',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('active', models.PositiveIntegerField(default=2)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('modified_on', models.DateTimeField(auto_now=True)),
                ('amount', models.DecimalField(null=True, max_digits=10, decimal_places=1, blank=True)),
                ('refund_date', models.DateTimeField()),
                ('refund_type', models.IntegerField(default=0)),
                ('refund_status', models.CharField(max_length=100, null=True, blank=True)),
                ('created_by', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
                ('customer', models.ForeignKey(blank=True, to='company.User_Profile', null=True)),
                ('shipment', models.ForeignKey(to='shipment.Shipment')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Truck_Driver_Payment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('active', models.PositiveIntegerField(default=2)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('modified_on', models.DateTimeField(auto_now=True)),
                ('transaction_status', models.CharField(max_length=100, null=True, blank=True)),
                ('transaction_type', models.CharField(max_length=100, null=True, blank=True)),
                ('transaction_id', models.CharField(max_length=100, null=True, blank=True)),
                ('transaction_date', models.DateTimeField(null=True, blank=True)),
                ('created_by', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
                ('shipment', models.OneToOneField(to='shipment.Shipment')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
