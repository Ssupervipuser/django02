from django.db import models


# Create your models here.

class Admin(models.Model):
    username = models.CharField(verbose_name="姓名", max_length=16)
    password = models.CharField(verbose_name="密码", max_length=64)

    def __str__(self):
        return self.username


class Department(models.Model):
    title = models.CharField(verbose_name="标题", max_length=32)

    def __str__(self):
        return self.title


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


class pretty_Num(models.Model):
    level_choice = (
        (1, '1级'),
        (2, '2级'),
        (3, '3级'),
        (4, '4级'),
        (5, '5级'),
    )
    status_choice = (
        (1, '启用'),
        (2, '禁用'),
    )
    mobile = models.CharField(max_length=11, verbose_name='手机号')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='价格', default=0)
    level = models.SmallIntegerField(verbose_name='靓号等级', choices=level_choice, default=1)
    status = models.SmallIntegerField(verbose_name='状态', choices=status_choice, default=1)


class Task(models.Model):
    """ 任务 """
    level_choices = (
        (1, "紧急"),
        (2, "重要"),
        (3, "临时"),
    )
    level = models.SmallIntegerField(verbose_name="级别", choices=level_choices, default=1)
    title = models.CharField(verbose_name="标题", max_length=64)
    detail = models.TextField(verbose_name="详细信息")
    user = models.ForeignKey(verbose_name="负责人", to="Admin", on_delete=models.CASCADE)


class Order(models.Model):
    """ 订单 """
    oid = models.CharField(verbose_name="订单号", max_length=64)
    title = models.CharField(verbose_name="名称", max_length=32)
    price = models.IntegerField(verbose_name="价格")

    status_choices = (
        (1, "待支付"),
        (2, "已支付"),
    )
    status = models.SmallIntegerField(verbose_name="状态", choices=status_choices, default=1)
    admin = models.ForeignKey(verbose_name="管理员", to="Admin", on_delete=models.CASCADE)

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
