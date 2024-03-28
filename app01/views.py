from django.shortcuts import render, redirect, HttpResponse
from app01 import models
from django import forms


# Create your views here.
# from app01.models import UserInfo


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
def depart_list(request):
    query_set = models.Department.objects.all()
    return render(request, 'depart_list.html', {'query_set': query_set})


def depart_add(request):
    if request.method == 'GET':
        return render(request, 'depart_add.html')
    title = request.POST.get("title")
    models.Department.objects.create(title=title)
    return redirect('/depart/list/')


def depart_delete(request):
    did = request.GET.get('did')
    models.Department.objects.filter(id=did).delete()
    return redirect('/depart/list/')


def depart_edit(request, eid):
    # eid = request.GET.get('eid')
    if request.method == 'GET':
        obj = models.Department.objects.filter(id=eid).first()
        return render(request, 'depart_edit.html', {'title': obj.title})
    title = request.POST.get('title')
    models.Department.objects.filter(id=eid).update(title=title)
    return redirect('/depart/list/')


#################User############################
def user_list(request):
    """ 用户管理 """
    # 获取已经有了session
    # print(request.session['user_info']['id'])
    # print(request.session['user_info']['username'])

    # print(request.unicom_userid)  # 来自中间件
    # print(request.unicom_username)

    # 获取所有用户列表 [obj,obj,obj]
    queryset = models.UserInfo.objects.all()

    # for obj in queryset:
    # print(obj.id, obj.name, obj.account, obj.create_time.strftime("%Y-%m-%d"), obj.gender, obj.get_gender_display(), obj.depart_id, obj.depart.title)
    """

    # 用Python的语法获取数据
        # print(obj.name, obj.depart_id)
        # obj.depart_id  # 获取数据库中存储的那个字段值
        # obj.depart.title  # 根据id自动去关联的表中获取哪一行数据depart对象。
    """
    return render(request, 'user_list.html', {"queryset": queryset})


def user_add(request):
    if request.method == 'GET':

        context = {
            'gender_choices': models.UserInfo.gender_choices,
            'depart_list': models.Department.objects.all(),
        }
        for obj in models.Department.objects.all():
            print(obj.title, obj.id)
            return render(request, 'user_add.html', context)
    user = request.POST.get('user')
    pwd = request.POST.get('pwd')
    age = request.POST.get('age')
    acount = request.POST.get('ac')
    ctime = request.POST.get('ctime')
    gender = request.POST.get('gd')
    depart = request.POST.get('dp')

    models.UserInfo.objects.create(name=user, password=pwd, age=age, account=acount,
                                   create_time=ctime, gender=gender, depart_id=depart)
    return redirect('/user/list/')


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


def user_modelform_add(request):
    if request.method == 'GET':
        form = userModelFrom()

        return render(request, 'user_modelfrom_add.html', {'form': form})

    # 用户post提交数据，数据校验
    form = userModelFrom(data=request.POST)
    if form.is_valid():  # 检查数据
        form.save()
        return redirect('/user/list/')

    return render(request, 'user_modelfrom_add.html', {'form': form})


def user_eidt(request, eid):
    row_obj = models.UserInfo.objects.filter(id=eid).first()
    if request.method == 'GET':
        # 根据id去数据库获取 要编辑的那一行数据
        forme = userModelFrom(instance=row_obj)

        return render(request, 'user_edit.html', {'frome': forme})

    forme = userModelFrom(data=request.POST, instance=row_obj)
    if forme.is_valid():
        # 默认保存的是用户输入的全部数据，如果如果想要用户输入以外的值
        # form.instance.字段名
        forme.save()
        return redirect('/user/list/')
    return render(request, 'user_edit.html', {'forme': forme})


def user_delete(request):
    did = request.GET.get('did')
    models.UserInfo.objects.filter(id=did).delete()
    return redirect('/user/list/')
#
#
# def depart_edit(request):
#     if request.method == "GET":
#         eid = request.GET.get('eid')
#         depart_obj = models.Department.objects.filter(id=eid).first()
#         context = {
#             'title': depart_obj.title,
#             'id': depart_obj.id
#         }
#         return render(request, 'depart_edit.html', context)
#     eid = request.GET.get('eid')
#     title = request.POST.get('title')
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
# def asset_add(request):
#     form = AssetModelform()
#     return render(request, 'asset_add.html', {'form': form})
