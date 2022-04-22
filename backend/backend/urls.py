'''
Author: DM
Email: simaoMi_DM@163.com
Description: 
Date: 2022-04-22 19:58:55
LastEditTime: 2022-04-22 20:20:54
Reference: 
'''

from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include('account.urls')),
]
