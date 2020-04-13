from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.http import HttpResponse
import requests
from django.conf import settings

# Create your views here.
class CreateCustomerView(TemplateView):
	template_name = 'user/customer_create.html'

	def get(self, request):
		if self.request.session.get('loged_in_user') == None:
			return redirect("login")
		data = {
			'email_id':self.request.session.get('loged_in_user'),
		}
		response = requests.get(settings.BASE_URL+'api/method/get-login-name/', data = data)
		return render(request,"user/customer_create.html",{"user_name":response.json()['full_name']})
