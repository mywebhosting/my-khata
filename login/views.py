from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import View, TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
import requests

# Create your views here.
'''
def index(request):
	# return HttpResponse("Worked")
	return render(request, 'user/login.html')

def check_login(request):
	return HttpResponse("Test")
'''
class IndexView(View):
	def get(seld, request):
		return HttpResponse("Landing page comming soon")

class LoginView(TemplateView):
	template_name = 'user/login.html'

class CheckLogin(View):
	def post(self, request):
		# response = requests.get('http://127.0.0.1:8000/api/login')
		# print (response)
		# print (response.status_code)
		# print (response.json())
		# print (request.POST.get('fname'))
		try:
			user_id = request.POST.get('user_id')
			password = request.POST.get('password')

			data = {
				'user_id':user_id,
				'password':password
			}
			# response = requests.post('http://127.0.0.1:8000/api/login', data = data)
			response = requests.post('http://127.0.0.1:8000/api/method/check-login/', data = data)
			# print (request.session['reset_user'])
			# print (response.json())
			if response.json() == 0:
				raise Exception("Login Id Invalide")
			elif(response.json() == 2):
				raise Exception("Password Invalide")
			elif(response.json() == 3):
				request.session['reset_user'] = user_id
				request.session.set_expiry(0)
				raise Exception("resetpassword")
			return HttpResponse("Success")
		except Exception as e:
			# print ("Error Message: "+str(e))
			return HttpResponse(e)

'''
class DashBoard(View):
	# template_name = "user/dashboard.html"
	def get(self, request):
		request.session.modified = True
		# request.session['member_id'] = "subhajit dey"
		# del request.session['member_id']
		# request.session.set_expiry(0)  # because by default set the expire date. But I need when browsr cloase then destroy
		# print (request.session.get_expire_at_browser_close())
		# return HttpResponse(request.session['member_id'])
		return HttpResponse("page comming soon")
'''

class ResetPwd(TemplateView):
	template_name = 'user/reset_password.html'

	'''
	# Not required in here, But it work
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['data'] = 'asdasd'
		print (self.request.session.get('reset_user'))		
		return context
	'''

	def get(self, request):
		if self.request.session.get('reset_user') == None:
			return redirect("login")
		else:
			return render(request,"user/reset_password.html",{"email_id":self.request.session.get('reset_user')})

	def post(self, request):
		password = request.POST.get('password')
		data = {
			"login_id": self.request.session.get('reset_user'),
			"new_password": password
		}
		response = requests.patch('http://127.0.0.1:8000/api/method/reset-password/', data = data)
		# status_code = response.json()['status_code']
		return HttpResponse(response.json()['status_code']);
