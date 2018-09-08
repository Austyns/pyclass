from rest_framework import serializers

from api.models import System_users, Subject, Accessment

# System Users 
class System_usersSerializer(serializers.ModelSerializer):
	class Meta:
		model = System_users
		fields = ('id', 'ad_name', 'ad_email', 'ad_role', 'ad_password', 'ad_phone', 'ad_status', 'ad_reg_at')


					
# Subject 
class SubjectSerializer(serializers.ModelSerializer):
	class Meta:
		model = Subject
		fields = ('id', 'name', 'discrip', 'cat_status', 'cat_slug', 'cat_reg_at', 'cat_reg_by')
	
		
					
# Accessments 
class AccessmentSerializer(serializers.ModelSerializer):
	class Meta:
		model = Accessment
		fields = ('id', 'user', 'subject', 'score', 'registered_at' )
	
