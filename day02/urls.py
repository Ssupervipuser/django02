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
from django.contrib import admin
from django.urls import path
from app01 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', views.login),

    path('depart/list/', views.depart_list),
    path('depart/add/', views.depart_add),
    path('depart/delete/', views.depart_delete),
    path('depart/<int:eid>/edit/', views.depart_edit),

    path('user/list/', views.user_list),
    path('user/add/', views.user_add),
    path('user/model/form/add/', views.user_modelform_add),
    path('user/<int:eid>/eid/', views.user_eidt),
    path('user/delete/', views.user_delete),

    path('pretty_num/list/', views.pretty_num_list),
    path('pretty_num/add/', views.pretty_num_add),
    path('pretty_num/<int:eid>/eid/', views.pretty_num_eidt),
    path('pretty_num/delete/', views.upretty_num_delete),

    # path('logout/', views.logout),

    # path('asset/list/', views.asset_list),
    # path('asset/add/', views.asset_add),
]
