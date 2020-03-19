from rest_framework import serializers
from login.models import LoginDetail

'''
class logincredential(serializers.ModelSerializer):
	class Meta:
		def natural_key(self):
        	return ('asd')
'''

class LoginDetailSerializer(serializers.ModelSerializer):
	class Meta:
		model = LoginDetail
		fields = ('login_detail_id','login_id','password','salt','account_type','account_id')