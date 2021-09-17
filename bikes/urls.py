from django.urls import path
from . import views
from .views import *

app_name = 'bikes'
urlpatterns = [
    path('', views.index, name='index'),
    path('service/', views.service, name='service'),
    path('blog/', views.blog, name='blog'),
    path('services', views.services, name='services'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('test/', views.test)
]