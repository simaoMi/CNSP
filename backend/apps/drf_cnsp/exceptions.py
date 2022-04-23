'''
Author: DM
Email: simaoMi_DM@163.com
Description: 
Date: 2022-04-23 19:38:53
LastEditTime: 2022-04-23 19:43:36
Reference: 
'''
from rest_framework.exceptions import APIException
from .response import failed


class CNSPAPIException(APIException):
    def __init__(self, detail=None, code=None):
        super().__init__(detail, code)


def exception_handler(exc, context):
    code, message = 400, '操作失败'
    
    return failed()
