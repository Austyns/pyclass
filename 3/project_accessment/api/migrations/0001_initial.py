# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-09-08 09:28
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Accessment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.CharField(blank=True, max_length=128)),
                ('registered_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, unique=True)),
                ('discrip', models.CharField(blank=True, max_length=128)),
                ('sub_reg_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='System_users',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('ad_name', models.CharField(max_length=128, unique=True)),
                ('ad_email', models.CharField(max_length=128, unique=True)),
                ('ad_password', models.CharField(max_length=256)),
                ('ad_phone', models.CharField(blank=True, max_length=30)),
                ('ad_status', models.CharField(blank=True, max_length=15)),
                ('ad_role', models.CharField(blank=True, max_length=15)),
                ('ad_reg_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AddField(
            model_name='accessment',
            name='subject',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Subject'),
        ),
        migrations.AddField(
            model_name='accessment',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.System_users'),
        ),
    ]