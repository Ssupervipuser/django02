from django import forms
from django.shortcuts import render, redirect

# Create your views here.
from app01 import models
from utils.encrpt import md5
from utils.img_code import check_code


class LoginForm(forms.Form):
    username = forms.CharField(label='用户名', widget=forms.TextInput)
    password = forms.CharField(label='用户名', widget=forms.PasswordInput)
    code = forms.CharField(label='验证码', widget=forms.TextInput)

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
        imgcode(request)
        form = LoginForm()
        return render(request, 'login.html', {'form': form})

    form = LoginForm(data=request.POST)
    if form.is_valid():

        # 验证码校验
        user_input_code = form.cleaned_data.pop('code')
        sys_code = request.session.get('image_code',"")
        if user_input_code.upper() != sys_code.upper():
            form.add_error('code', '验证码错误')
            return render(request, 'login.html', {'form': form})

        # 去数据库校验用户名和密码是否正确，获取用户对象、None
        # admin_object = models.Admin.objects.filter(username=xxx, password=xxx).first()
        admin_object = models.Admin.objects.filter(**form.cleaned_data).first()

        if not admin_object:  # 找不到则为none
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


def imgcode(request):
    # 调用pillow函数，生成图片
    img, code_string = check_code()
    print(code_string)
    # 写入到自己的session中（以便于后续获取验证码再进行校验）
    request.session['image_code'] = code_string
    # 给Session设置60s超时
    request.session.set_expiry(60)

    with open('static/images/code.png', 'wb', ) as f:
        img.save(f, format='png')





