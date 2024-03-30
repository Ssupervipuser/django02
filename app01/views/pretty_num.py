from django.shortcuts import render, redirect
from app01 import models

from utils.MyModelForm import numFromModel, numEditFromModel


def pretty_num_list(request):
    data_dict = {}
    search_data = request.GET.get("q")
    if search_data:
        data_dict["mobile__contains"] = search_data
    # queryset = models.pretty_Num.objects.all().order_by('-level')
    queryset = models.pretty_Num.objects.filter(**data_dict).order_by('-level')
    return render(request, 'pretty_num.html', {'queryset': queryset})


def pretty_num_add(request):
    if request.method == 'GET':
        form = numFromModel()

        return render(request, 'pretty_add.html', {'form': form})
    form = numFromModel(data=request.POST)
    if form.is_valid():
        form.save()
        return redirect('/pretty_num/list/')
    return render(request, 'pretty_add.html', {'form': form})


def pretty_num_eidt(request, eid):
    row_obj = models.pretty_Num.objects.filter(id=eid).first()
    if request.method == 'GET':
        form = numEditFromModel(instance=row_obj)
        return render(request, 'pretty_edit.html', {'form': form})

    form = numEditFromModel(data=request.POST, instance=row_obj)
    if form.is_valid():
        form.save()
        return redirect('/pretty_num/list/')
    return render(request, 'pretty_edit.html', {'form': form})


def upretty_num_delete(request):
    did = request.GET.get('did')
    models.pretty_Num.objects.filter(id=did).delete()
    return redirect('/pretty_num/list/')
