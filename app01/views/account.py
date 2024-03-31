from django import forms
from django.shortcuts import render, redirect

# Create your views here.
from app01 import models
from utils.encrpt import md5


class LoginForm(forms.Form):
    username = forms.CharField(label='用户名', widget=forms.TextInput)
    password = forms.CharField(label='用户名', widget=forms.PasswordInput)

    def clean_password(self):
        pwd = self.cleaned_data.get('password')
        return md5(pwd)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for name, field in self.fields.items():
            # 添加样式装饰
            field.widget.attrs = {'class': 'form-control', 'placeholder': field.label}


def login(request):

    if request.method == 'GET':
        form = LoginForm()
        return render(request, 'login.html', {'form': form})

    form = LoginForm(data=request.POST)
    if form.is_valid():
        # 去数据库校验用户名和密码是否正确，获取用户对象、None
        # admin_object = models.Admin.objects.filter(username=xxx, password=xxx).first()
        admin_object = models.Admin.objects.filter(**form.cleaned_data).first()
        if not admin_object: #找不到则为none
            form.add_error("password", "用户名或密码错误")
            # form.add_error("username", "用户名或密码错误")
            return render(request, 'login.html', {'form': form})
        # 用户名和密码正确
        # 网站生成随机字符串; 写到用户浏览器的cookie中；在写入到session中；
        request.session["info"] = {'id': admin_object.id, 'name': admin_object.username}
        # session可以保存7天
        request.session.set_expiry(60 * 60 * 24 * 7)
        return redirect('/admin/list/')
    form.add_error("password", "用户名或密码错误")
    return render(request, 'login.html', {'form': form})


def logout(request):
    request.session.clear()
    return redirect('/login/')




# def asset_list(request):
#     query_set = models.Asset.objects.all().order_by('-id')
#     return render(request, 'asset_list.html', {'query_set': query_set})
#
#
# class AssetModelform(forms.ModelForm):
#     class Meta:
#         model = models.Asset
#         # fields = '__all__'
#         fields = ["name", "price", "category", "depart"]
#
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         for name, field in self.fields.items():
#             field.widget.attrs['class'] = "form-control"
#
#
# def asset_add(request):
#     form = AssetModelform()
#     return render(request, 'asset_add.html', {'form': form})
