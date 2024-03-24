from django.shortcuts import render, redirect, HttpResponse
from app01 import models
from django import forms


# Create your views here.
def login(req):
    if req.method == 'GET':
        return render(req, 'login.html')
    user = req.POST.get('username')
    pwd = req.POST.get('pwd')
    admin_object = models.Admin.objects.filter(username=user, password=pwd).first()

    if admin_object:
        # 设置session
        req.session['user_info'] = {'id': admin_object.id, 'username': admin_object.username}
        return redirect('/user/list/')

    return render(req, 'login.html', {'error': "用户名或密码错误"})

#
# def logout(req):
#     req.session.clear()
#     return redirect('/login/')
#
#
# def depart_list(req):
#     # 获取已经有了session
#     # print(req.session['user_info']['id'])
#     # print(req.session['user_info']['username'])
#
#     # print(req.unicom_userid)  # 来自中间件
#     # print(req.unicom_username)
#     query_set = models.Department.objects.all().order_by("-id")
#
#     return render(req, 'depart_list.html', {'username': req.unicom_username, 'query_set': query_set})
#
#
# def depart_add(request):
#     if request.method == 'GET':
#         return render(request, 'depart_add.html')
#
#     title = request.POST.get('title')
#     models.Department.objects.create(title=title)
#     return redirect('/depart/list/')
#
#
# def depart_delete(request):
#     did = request.GET.get('did')
#     models.Department.objects.filter(id=did).delete()
#     return redirect('/depart/list/')
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
# def asset_list(req):
#     query_set = models.Asset.objects.all().order_by('-id')
#     return render(req, 'asset_list.html', {'query_set': query_set})
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
