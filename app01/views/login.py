from django.shortcuts import render


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
