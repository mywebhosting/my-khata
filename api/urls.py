from django.urls import path
from api import views

app_name = 'api'

urlpatterns = [
	path('check-login/', views.LoginCredentialCheck.as_view()),
	path('reset-password/', views.ResetPassword.as_view()),
]