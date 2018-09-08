# from django.conf.urls import url, include

from django.conf.urls import  url, include
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework import routers
from api import views

from rest_framework.schemas import get_schema_view


urlpatterns = [
                
                # url(r'^doc/$', schema_view),
		# System Admins 
		url(r'^systemAdmins/$', views.systemAdmins.as_view()),
                url(r'^systemAdmin/(?P<pk>.+)/$', views.systemAdminDetails.as_view()), 
                url(r'^login/?$', views.loginUser.as_view()), 

                # subject
                url(r'^subjects/?$', views.subjects.as_view()),
                url(r'^subject/(?P<pk>[0-9]+)/$', views.subjectDetails.as_view()), 

                # accessment
                url(r'^accessment/?$', views.accessments.as_view()),
                url(r'^accessments/(?P<pk>.+)/$', views.accessmentDetails.as_view()), 


                ]
urlpatterns = format_suffix_patterns(urlpatterns)