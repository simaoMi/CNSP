'''
Author: DM
Email: simaoMi_DM@163.com
Description: 
Date: 2022-04-22 20:18:54
LastEditTime: 2022-04-22 20:22:04
Reference: 
'''
from django.urls import path
from . import views

urlpatterns = [
  path('', views.test),
]