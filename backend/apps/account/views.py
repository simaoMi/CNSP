'''
Author: DM
Email: simaoMi_DM@163.com
Description: 
Date: 2022-04-22 20:17:23
LastEditTime: 2022-04-22 20:20:15
Reference: 
'''
from django.http import JsonResponse


def test(request):
  return JsonResponse({'code':200, 'message': 'ok'})