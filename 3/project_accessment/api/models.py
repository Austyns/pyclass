from __future__ import unicode_literals

from django.db import models

from datetime import datetime
from decimal import Decimal
import uuid

# Authentication Params 
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.conf import settings



# System Users  

class System_users(models.Model): 
	id = models.UUIDField(primary_key=True, default=uuid.uuid4)
	ad_name = models.CharField(max_length=128, unique=True) 
	ad_email = models.CharField(max_length=128, unique=True) 
	ad_password = models.CharField(max_length=256) 
	ad_phone = models.CharField(max_length=30, blank=True)
	ad_status = models.CharField(max_length=15, blank=True)
	ad_role = models.CharField(max_length=15, blank=True)
	ad_reg_at = models.DateTimeField(auto_now_add=True)

	def __str__(self): #For Python 3, use __unicode__ on Python 2

		return self.ad_name


# Subjects 

class Subject(models.Model): 
	name = models.CharField(max_length=256, unique=True) 
	discrip = models.CharField(max_length=128, blank=True) 
	sub_reg_at = models.DateTimeField(auto_now_add=True)

	def __str__(self): #For Python 3, use __unicode__ on Python 2

		return self.cat_name


# Accessments
class Accessment(models.Model): 
	user = models.ForeignKey(System_users) 
	subject = models.ForeignKey(Subject) 
	score = models.CharField(max_length=128, blank=True)
	registered_at = models.DateTimeField(auto_now_add=True)

	def __str__(self): #For Python 3, use __unicode__ on Python 2

		return self.name


################################
##### USERS TOKEN GENERATOR ####
################################

# This code is triggered whenever a new user has been created and saved to the database

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
	if created:
		Token.objects.create(user=instance)


