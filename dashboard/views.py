from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import View, TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
import requests

from django.conf import settings

# Create your views here.
class DashboardView(TemplateView):
	template_name = 'user/dashboard.html'
	# def get(self, request):
	# 	return HttpResponse("New dashboard comming soon")

	'''
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['user_name'] = "Test user name"
		return context
	'''

	def get(self, request):
		if self.request.session.get('loged_in_user') == None:
			return redirect("login")
		data = {
			'email_id':self.request.session.get('loged_in_user'),
		}
		response = requests.get(settings.BASE_URL+'api/method/get-login-name/', data = data)
		return render(request,"user/dashboard.html",{"user_name":response.json()['full_name']})