# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('active', models.PositiveIntegerField(default=2)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('modified_on', models.DateTimeField(auto_now=True)),
                ('object_id', models.TextField(verbose_name='object ID')),
                ('notification_type', models.IntegerField(default=0)),
                ('comment', models.CharField(max_length=255, null=True, blank=True)),
                ('submit_date', models.DateTimeField(auto_now_add=True)),
                ('is_seen', models.BooleanField(default=False)),
                ('content_type', models.ForeignKey(related_name='django_content_type_set_for_notification', verbose_name='content type', to='contenttypes.ContentType')),
                ('nt_from', models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Notification_History',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('seen', models.BooleanField(default=False)),
                ('notification', models.ForeignKey(blank=True, to='notifications.Notification', null=True)),
                ('to', models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
        ),
    ]
