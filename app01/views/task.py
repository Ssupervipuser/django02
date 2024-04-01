import json

from django.forms import forms
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from app01 import models
from utils import form


class TaskModelForm(form.myModelForm):
    class Meta:
        model = models.Task
        fields = "__all__"


def task_list(request):
    """ 任务列表 """
    # 去数据库获取所有的任务
    queryset = models.Task.objects.all().order_by('-id')

    form = TaskModelForm()

    context = {
        "form": form,
        "queryset": queryset,  # 分完页的数据

    }
    return render(request, "task_list.html", context)


@csrf_exempt
def task_add(request):
    # {'level': ['1'], 'title': ['sdfsdfsdfsd'], 'detail': ['111'], 'user': ['8']}
    # print(request.POST)

    # 1.用户发送过来的数据进行校验（ModelForm进行校验）
    form = TaskModelForm(data=request.POST)
    if form.is_valid():
        form.save()
        data_dict = {"status": True}
        return HttpResponse(json.dumps(data_dict))

    data_dict = {"status": False, 'error': form.errors}
    return HttpResponse(json.dumps(data_dict, ensure_ascii=False))


# 测试
@csrf_exempt
def task_ajax(request):
    print(request.GET)
    print(request.POST)

    data_dict = {"status": True, 'data': [11, 22, 33, 44]}
    return HttpResponse(json.dumps(data_dict))


# class AssetModelform(forms.ModelForm):
#     class Meta:
#         model = models.Task
#         # fields = '__all__'
#         fields = ["name", "price", "category", "depart"]
#
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         for name, field in self.fields.items():
#             field.widget.attrs['class'] = "form-control"
#
#
def task_add(request):
    return render(request, 'asset_add.html')
