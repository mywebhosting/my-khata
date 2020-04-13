from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.http import HttpResponse
import requests

# from django.conf import settings
from django.core.files.storage import FileSystemStorage

from django.core.files.base import ContentFile

import base64
from django.conf import settings

# Create your views here.
class CreateItem(TemplateView):
	template_name = 'user/item_create.html'

	def get(self, request):
		if self.request.session.get('loged_in_user') == None:
			return redirect("login")
		data = {
			'email_id':self.request.session.get('loged_in_user'),
		}
		response = requests.get(settings.BASE_URL+'api/method/get-login-name/', data = data)
		return render(request,"user/item_create.html",{"user_name":response.json()['full_name']})

	def post(self, request):
		'''
		myfile = request.FILES['upload_product_image']
		fs = FileSystemStorage()
		filename = fs.save("product/sadsad"+myfile.name, myfile)
		uploaded_file_url = fs.url(filename)
		print (uploaded_file_url)
		'''
		# image = request.FILES['upload_product_image']
		# print (image)
		# data = {
		# 	'image_name':request.FILES['upload_product_image'],
		# }
		# resp = requests.post('http://127.0.0.1:8000/api/method/insert-product/', data = data)
		product_name = request.POST.get('product_name')
		quantity_type = request.POST.get('quantity_type')
		quantity = request.POST.get('quantity')
		price = request.POST.get('price')
		product_img_name = request.POST.get('product_img_name')
		product_img_data = request.POST.get('product_img_data')

		data = {
			"product_name": product_name,
			"quantity_type": quantity_type,
			"quantity": quantity,
			"price": price,
			"product_img_name": product_img_name,
			"product_img_data": product_img_data,
			"product_added_by": self.request.session.get('loged_in_user')
		}

		resp = requests.post(settings.BASE_URL+'api/method/insert-product/', data = data)
		status_code = resp.json()['status_code']

		return HttpResponse(status_code)
