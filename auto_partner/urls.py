from django.urls import path
from . import views

app_name = 'auto_partner'
urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login_request, name='login'),
    path('logout/', views.logout_request, name='logout'), 
    path('', views.base, name='base'),
    path('auto/<str:auto_id>', views.get_auto),
    path('auto/', views.create_auto),
]

