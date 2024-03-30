from django.shortcuts import render, redirect

from app01 import models


def admin_list(request):
    if request.method == 'GET':
        query_set = models.Admin.objects.all()
        return render(request, 'admin_list.html', {'queryset': query_set})
