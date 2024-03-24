from django.shortcuts import render, redirect, HttpResponse
from app01 import models
from django import forms


# Create your views here.
def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    # user = request.POST.get('username')
    # pwd = request.POST.get('pwd')
    # admin_object = models.Admin.objects.filter(username=user, password=pwd).first()

    # if admin_object:
    #     # 设置session
    #     request.session['user_info'] = {'id': admin_object.id, 'username': admin_object.username}
    #     return redirect('/user/list/')

    return render(request, 'login.html', {'error': "用户名或密码错误"})

#
# def logout(request):
#     request.session.clear()
#     return redirect('/login/')
#
#
def info_list(request):
    # 获取已经有了session
    # print(request.session['user_info']['id'])
    # print(request.session['user_info']['username'])

    # print(request.unicom_userid)  # 来自中间件
    # print(request.unicom_username)
    query_set = models.UserInfo.objects.all().order_by("-id")

    return render(request, 'info_list.html', {'username': request, 'data_list': query_set})


def info_add(requestuest):
    if requestuest.method == 'GET':
        return render(requestuest, 'info_add.html')

    user = requestuest.POST.get('user')
    pwd = requestuest.POST.get('pwd')
    age = requestuest.POST.get('age')
    models.UserInfo.objects.create(name=user,password=pwd,age=age)
    return redirect('/info/list/')


def info_delete(requestuest):
    did = requestuest.GET.get('did')
    models.UserInfo.objects.filter(id=did).delete()
    return redirect('/info/list/')
#
#
# def depart_edit(requestuest):
#     if requestuest.method == "GET":
#         eid = requestuest.GET.get('eid')
#         depart_obj = models.Department.objects.filter(id=eid).first()
#         context = {
#             'title': depart_obj.title,
#             'id': depart_obj.id
#         }
#         return render(requestuest, 'depart_edit.html', context)
#     eid = requestuest.GET.get('eid')
#     title = requestuest.POST.get('title')
#     models.Department.objects.filter(id=eid).update(title=title)
#     return redirect('/depart/list/')
#
#
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
# def asset_add(requestuest):
#     form = AssetModelform()
#     return render(requestuest, 'asset_add.html', {'form': form})
