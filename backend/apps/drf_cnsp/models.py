from django.db import models
from django.conf import settings


class BaseModel(models.Model):
    id = models.BigAutoField(primary_key=True, help_text="Id", verbose_name="Id")
    description = models.CharField(max_length=255, verbose_name="描述", null=True, blank=True, help_text="描述")
    creator = models.ForeignKey(to=settings.AUTH_USER_MODEL, related_query_name='creator_query', null=True,
                                verbose_name='创建人', help_text="创建人", on_delete=models.SET_NULL, db_constraint=False)
    modifier = models.CharField(max_length=255, null=True, blank=True, help_text="修改人", verbose_name="修改人")
    update_datetime = models.DateTimeField(
        auto_now=True, null=True, blank=True, help_text="修改时间", verbose_name="修改时间"
    )
    create_datetime = models.DateTimeField(
        auto_now_add=True, null=True, blank=True, help_text="创建时间", verbose_name="创建时间"
    )

    class Meta:
        abstract = True
        verbose_name = verbose_name_plural = '基类模型'
