from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from django.shortcuts import render, redirect, HttpResponse
from app01 import models
from django import forms



########################ModelFrom##################################

class userModelFrom(forms.ModelForm):
    class Meta:
        # 注意是model
        model = models.UserInfo
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for name, field in self.fields.items():
            # 添加样式装饰
            field.widget.attrs = {'class': 'form-control', 'placeholder': field.label}



#########################################prettyNUM##############
class numFromModel(forms.ModelForm):
    # 验证方式1
    mobile = forms.CharField(
        label='手机号',
        validators=[RegexValidator(regex=r'^1[3-9]\d{9}$', message='手机号格式错误')]
    )

    class Meta:
        model = models.pretty_Num
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for name, field in self.fields.items():
            # 添加样式装饰
            field.widget.attrs = {'class': 'form-control', 'placeholder': field.label}

    # 验证方式2
    def clean_mobile(self):
        text_num = self.cleaned_data["mobile"]
        # 判断手机号是否存在
        exists = models.pretty_Num.objects.filter(mobile=text_num).exists()
        if exists:
            raise ValidationError('手机号已存在')
        return text_num




class numEditFromModel(forms.ModelForm):
    # 验证方式1
    mobile = forms.CharField(
        label='手机号',
        validators=[RegexValidator(regex=r'^1[3-9]\d{9}$', message='手机号格式错误')]
    )
    class Meta:
        model = models.pretty_Num
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for name, field in self.fields.items():
            # 添加样式装饰
            field.widget.attrs = {'class': 'form-control', 'placeholder': field.label}

    # 验证方式2
    def clean_mobile(self):
        text_num = self.cleaned_data["mobile"]
        # id!=自己 and mobile已经存在
        exists = models.pretty_Num.objects.exclude(id=self.instance.pk).filter(mobile=text_num).exists()
        if exists:
            raise ValidationError('手机号已存在e')
        return text_num
