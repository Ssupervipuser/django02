from django.db import models


# Create your models here.

class Department(models.Model):
    title = models.CharField(verbose_name="标题", max_length=32)


#
#     def __str__(self):
#         return self.title


class UserInfo(models.Model):
    """ 员工表 """
    gender_choices = (
        (1, "男"),
        (2, "女"),
    )
    name = models.CharField(verbose_name="姓名", max_length=16)
    password = models.CharField(verbose_name="密码", max_length=64)
    age = models.IntegerField(verbose_name="年龄")
    account = models.DecimalField(verbose_name="账户余额", max_digits=10, decimal_places=2, default=0)
    create_time = models.DateTimeField(verbose_name="入职时间")

    depart = models.ForeignKey(to="Department", to_field="id", on_delete=models.CASCADE)

    gender = models.SmallIntegerField(verbose_name="性别", choices=gender_choices)

# class Admin(models.Model):
#     username = models.CharField(verbose_name="用户名", max_length=16)
#     password = models.CharField(verbose_name="密码", max_length=64)
#
#

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
