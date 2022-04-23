'''
Author: DM
Email: simaoMi_DM@163.com
Description: 
Date: 2022-04-23 19:07:27
LastEditTime: 2022-04-23 19:35:27
Reference: 
'''
from rest_framework import status
# from rest_framework.response import Response    # 返回存在问题
from django.http import JsonResponse


def _response(data, code, message, success):
    result = dict()

    result['code'] = code
    result['message'] = message
    result['success'] = success

    if data is not None:
        result['data'] = data
    return JsonResponse(data=result, status=code)


def success(data=None, code=status.HTTP_200_OK, message='请求成功!', success=True):
    return _response(data, code, message, success)


def failed(data=None, code=status.HTTP_400_BAD_REQUEST, message='操作失败!', success=False):
  return _response(data, code, message, success)
