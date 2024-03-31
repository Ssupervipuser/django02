from django.shortcuts import render, redirect
from app01 import models


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



