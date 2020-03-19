from django.shortcuts import render
from django.http import HttpResponse

from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from login.models import LoginDetail, AccountStatus, ShopKeeperAccount
from . apiserializer import LoginDetailSerializer
from . password_hash import *

from django.db import connection

# Create your views here.

class LoginCredentialCheck(APIView):
	def get(self, request):
		'''
		employee1 = employees.objects.all()
		serializer = logincredential(employee1, many=True)
		print (request.GET)
		'''

		data = {'test':'Test data'}
		return Response(data)

	def post(self, request):
		user_id = request.POST.get('user_id')
		password = request.POST.get('password')
		# iterations = PBKDF2PasswordHasher.iterations * 100
		# print(iterations)
		# test2 = super().encode(sha1_hash, 'salt', iterations)
		# print (test2)
		# test2 = hashlib.sha224(password.encode())
		# print (test2.hexdigest())		

		login_detl_count = LoginDetail.objects.filter(login_id=user_id,).count()
		if login_detl_count:
			login_detl = LoginDetail.objects.all()
			serializer = LoginDetailSerializer(login_detl, many=True)
			# print (serializer.data)
			data_tup = serializer.data[0]
			find_salt = data_tup['salt']
			saved_password = data_tup['password']
			encypt_password = make_encrypt(password,find_salt)

			if saved_password == encypt_password:
				# request.session['login_user'] = "sdmk"
				# request.session.set_expiry(0)
				acc_status_obj = CheckAccountStatus()
				acc_status = acc_status_obj.check(serializer.data[0]['login_id'])
				if acc_status == 1:
					return Response(3)
				return Response(1)
			else:
				return Response(2)
		return Response(0)

class CheckAccountStatus:
	def __init__(self):
		# login_detl = LoginDetail.objects.raw("SELECT account_id as id FROM shop_keeper_account shop, account_status acc_s WHERE shop.status_id_id = acc_s.status_id AND acc_s.status_name = 'Reset' AND shop.email_id = %s", [user_id])
		# print (login_detl.columns)
		# print (len(list(login_detl.columns)))
		# print (count(login_detl))
		# for p in login_detl:
		# 	print (p.columns)
		pass

		
	def check(self, user_id):
		cursor = connection.cursor()
		cursor.execute('''SELECT account_id as id FROM shop_keeper_account shop, account_status acc_s WHERE shop.status_id_id = acc_s.status_id AND acc_s.status_name = 'Reset' AND shop.email_id = %s''',[user_id])
		# row = cursor.fetchone()
		row = cursor.fetchall()
		return len(row)

class ResetPassword(APIView):
	def patch(self, request):
		try:
			login_id = request.POST.get('login_id')
			password = request.POST.get('new_password')
			get_salt = LoginDetail.objects.values_list('salt').filter(login_id=login_id)[0][0]
			encypt_password = make_encrypt(raw_password=password,salt=get_salt)
			get_status_id = AccountStatus.objects.values_list('status_id').filter(status_name='Active')[0][0]
			password_change_resp = LoginDetail.objects.filter(login_id=login_id).update(password=encypt_password)
			account_status_resp = ShopKeeperAccount.objects.filter(email_id=login_id).update(status_id=get_status_id)
			if account_status_resp == 1:
				return Response({"status_code":1,"status_msg":"Password Reset"})
			else:
				return Response({"status_code":0,"status_msg":"Something was wrong!"})
		except Exception as e:
			return e
