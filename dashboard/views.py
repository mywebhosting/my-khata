from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View, TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
import requests

# Create your views here.
class DashboardView(TemplateView):
	template_name = 'user/dashboard.html'
	# def get(self, request):
	# 	return HttpResponse("New dashboard comming soon")

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['user_name'] = "Test user name"
		return context