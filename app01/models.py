from django.db import models


# Create your models here.

class UserInfo(models.Model):
    name=models.CharField(max_length=32)
    password=models.CharField(max_length=32)
    age=models.IntegerField()














# class Admin(models.Model):
#     username = models.CharField(verbose_name="用户名", max_length=16)
#     password = models.CharField(verbose_name="密码", max_length=64)
#
#
# class Department(models.Model):
#     title = models.CharField(verbose_name="标题", max_length=16)
#
#     def __str__(self):
#         return self.title
#
#
# class Asset(models.Model):
#     name = models.CharField(verbose_name="名称", max_length=32)
#     price = models.IntegerField(verbose_name="价格")
#     category = models.SmallIntegerField(verbose_name="类型", choices=(
#         (1, '办公类'),
#         (2, '3C类'),
#         (3, '房产'),
#     ))
#     # 数据库中depart_id
#     depart = models.ForeignKey(verbose_name="所属部门", to="Department", to_field="id", on_delete=models.CASCADE)
