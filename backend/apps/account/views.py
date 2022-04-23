'''
Author: DM
Email: simaoMi_DM@163.com
Description: 
Date: 2022-04-22 20:17:23
LastEditTime: 2022-04-23 19:18:53
Reference: 
'''
import logging
from apps.drf_cnsp.response import success


logger = logging.getLogger('default')


def test(request):
  logger.info(request)
  return success()