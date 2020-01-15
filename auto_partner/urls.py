from django.urls import path
from . import views

app_name = 'auto_partner'
urlpatterns = [
    path('', views.login, name='login'),
]

