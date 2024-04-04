"""
URL configuration for day02 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.contrib import admin
from django.urls import path, re_path
from django.views.static import serve

from app01.views import user, pretty_num, depart, admin, account, task, order, chart, upload

urlpatterns = [
    # path('admin/', admin.site.urls),

    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}, name='media'),
    path('login/', account.login),
    path('logout/', account.logout),
    path('image/code/', account.imgcode),

    path('admin/list/', admin.admin_list),
    path('admin/add/', admin.admin_add),
    path('admin/<int:eid>/edit/', admin.admin_edit),
    path('admin/delete/', admin.admin_delete),

    path('depart/list/', depart.depart_list),
    path('depart/add/', depart.depart_add),
    path('depart/delete/', depart.depart_delete),
    path('depart/<int:eid>/edit/', depart.depart_edit),

    path('user/list/', user.user_list),
    path('user/add/', user.user_add),
    path('user/model/form/add/', user.user_modelform_add),
    path('user/<int:eid>/eid/', user.user_eidt),
    path('user/delete/', user.user_delete),

    path('pretty_num/list/', pretty_num.pretty_num_list),
    path('pretty_num/add/', pretty_num.pretty_num_add),
    path('pretty_num/<int:eid>/eid/', pretty_num.pretty_num_eidt),
    path('pretty_num/delete/', pretty_num.upretty_num_delete),

    path('task/list/', task.task_list),
    path('task/add/', task.task_add),

    path('order/list/', order.order_list),
    path('order/add/', order.order_add),
    path('order/delete/', order.order_delete),
    path('order/detail/', order.order_detail),
    path('order/edit/', order.order_edit),

    path('chart/list/', chart.chart_list),
    path('chart/bar/', chart.chart_bar),
    path('chart/pie/', chart.chart_pie),
    path('chart/line/', chart.chart_line),

    path('upload/list/', upload.upload_list),
    path('upload/form/', upload.upload_form),
    path('upload/model/form/', upload.upload_modal_form),

    # 测试ajax
    path('task/ajax/', task.task_ajax),

]
