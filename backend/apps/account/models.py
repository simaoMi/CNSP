from django.db import models
from django.contrib.auth.hashers import make_password, check_password
from drf_cnsp.models import BaseModel


class UserModel(BaseModel):

    GENDER_CHOICES = (
        ('n', '男'),
        ('v', '女'),
        ('o', '未知'),
    )
    username = models.CharField(max_length=32, verbose_name='真实姓名', blank=True, null=True)
    mobile = models.CharField(max_length=11, unique=True, verbose_name='手机号', null=False)
    _password = models.CharField(max_length=255, verbose_name='哈希密码')
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, default='o', verbose_name='性别')

    class Meta:
        db_table = 'cnsp_user'
        verbose_name = verbose_name_plural = '用户信息表'

    def __str__(self):
        return self.mobile

    @property
    def password(self):
        raise AttributeError('该属性不可读')

    @password.setter
    def password(self, row_password):
        self._password = make_password(row_password)

    def password_validate(self, password):
        return check_password(password, self._password)
