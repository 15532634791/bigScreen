from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    """
    用户信息模型
    """

    class Meta:
        db_table = "userInfo"
        verbose_name = "用户信息表"
        verbose_name_plural = '用户信息表'
