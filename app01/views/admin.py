from django import forms
from django.core.exceptions import ValidationError
from django.shortcuts import render, redirect
from app01.models import Admin
from app01 import models
from utils.encrpt import md5

from utils.form import myModelForm


def admin_list(request):
    if request.method == 'GET':
        query_set = models.Admin.objects.all()
        return render(request, 'admin_list.html', {'queryset': query_set})


class AdminModelForm(myModelForm):
    confirm_password = forms.CharField(
        label='确认密码',
        widget=forms.PasswordInput
    )

    class Meta:
        model = Admin
        fields = '__all__'

        widgets = {
            'password': forms.PasswordInput
        }

    def clean_password(self):
        pwd = self.cleaned_data.get('password')
        return md5(pwd)

    def clean_confirm_password(self):
        pwd = self.cleaned_data.get('password')

        confrim = md5(self.cleaned_data.get('confirm_password'))
        if pwd != confrim:
            raise ValidationError('两次输入密码不一致')
        return confrim


def admin_add(request):
    title = '新建管理员'
    if request.method == 'GET':
        form = AdminModelForm()
        return render(request, 'change.html', {'form': form, 'title': title})

    form = AdminModelForm(data=request.POST)
    # username = request.POST.get('username')
    # password = request.POST.get('password')
    # models.Admin.objects.create(username=username, password=password)
    if form.is_valid():
        form.save()
        return redirect('/admin/list/')

    return render(request, 'change.html', {'form': form, 'title': title})


def admin_edit(request, eid):
    title = '编辑管理员'
    row_obj = models.Admin.objects.filter(id=eid).first()
    if request.method == 'GET':
        form = AdminModelForm(instance=row_obj)
        return render(request, 'change.html', {'form': form, 'title': title})
    # form=AdminModelForm(request.POST,instance=)

    form=AdminModelForm(data=request.POST,instance=row_obj)
    if form.is_valid():
        form.save()
        return redirect('/admin/list/')
    return render(request, 'change.html', {'title': title})


def admin_delete(request):
    did = request.GET.get('did')
    models.Admin.objects.filter(id=did).delete()
    return redirect('/admin/list/')
