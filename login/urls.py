from django.urls import path
from login import views

app_name = 'login'

urlpatterns = [
    # path('index/', views.index2, name="index2"),
    # path('check-login/', views.check_login, name="check_login"),
    path('check-login/', views.CheckLogin.as_view(), name="check_login"),
    path('reset-password/', views.ResetPwd.as_view(), name="reset_pwd"),

    # path('dash-board/', views.DashBoard.as_view(), name="dash_board"),

]