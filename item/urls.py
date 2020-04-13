from django.urls import path
from item import views

app_name = 'item'

urlpatterns = [
	path('create/', views.CreateItem.as_view(), name='create_item'),
]