from django.urls import path
from api import views

app_name = 'api'

urlpatterns = [
	path('check-login/', views.LoginCredentialCheck.as_view()),
	path('reset-password/', views.ResetPassword.as_view()),
	path('get-login-name/', views.GetLoginName.as_view()),
	path('insert-product/', views.InsertProduct.as_view()),
]