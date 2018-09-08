from django.shortcuts import render
from django.db import connections
from rest_framework import generics
from rest_framework.generics import RetrieveUpdateDestroyAPIView

from rest_framework.decorators import api_view
from rest_framework.viewsets import ModelViewSet


from rest_framework import filters
from rest_framework.response import Response
from django.http import HttpResponse, JsonResponse
import requests
import json


from api.models import System_users, Subject, Accessment

from api.serializers import System_usersSerializer, SubjectSerializer, AccessmentSerializer

import hashlib, uuid

SALT_STR = "3442edfdgdh273yy3nBHD4jfhbdn-DJndjdn9jf3938jndcucjm-mdjdnueen-D4Hflsd#udy@ndnd_MDMDiedm3984hn0jkjn"


# Create your views here.

#System Administrators  
class systemAdmins(generics.ListCreateAPIView):
	queryset = System_users.objects.all()
	serializer_class = System_usersSerializer

	def post(self, request, *args, **kwargs):
		hashed = hashlib.sha512(request.data['ad_password'] + SALT_STR).hexdigest()
		request.data['ad_password'] = hashed
		return self.create(request, *args, **kwargs)


class systemAdminDetails(generics.RetrieveUpdateAPIView):
	queryset = System_users.objects.all()
	serializer_class = System_usersSerializer

# User Login
class loginUser(generics.ListCreateAPIView):
	serializer_class = System_usersSerializer 

	def post(self, request, *args, **kwargs):
		email = request.data.get('ad_email')
		password = request.data.get('ad_pass')
		hashed = hashlib.sha512(str(password) + SALT_STR).hexdigest()
		user = System_users.objects.filter(ad_email=email, ad_password=hashed).values()

		return JsonResponse({"data": list(user)})


# Subject  
class subjects(generics.ListCreateAPIView):
	queryset = Subject.objects.all()
	serializer_class = SubjectSerializer

class subjectDetails(generics.RetrieveUpdateDestroyAPIView):
	queryset = Subject.objects.all()
	serializer_class = SubjectSerializer



# Accessment  
class accessments(generics.ListCreateAPIView):
	queryset = Accessment.objects.all()
	serializer_class = AccessmentSerializer

class accessmentDetails(generics.RetrieveUpdateDestroyAPIView):
	queryset = Accessment.objects.all()
	serializer_class = AccessmentSerializer

