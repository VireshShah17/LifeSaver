from django.urls import path
from . import views

app_name = 'index'
urlpatterns = [
    path('', views.index, name='index'),
    path('contact/', views.contact , name='contact'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
]