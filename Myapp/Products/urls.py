"""Myblog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path,include

from . views import ProductCreat,producList,ProductUpdate,ProductDetail,ProducttDel


urlpatterns = [
    path('', producList.as_view(),name='pl'),
    path('pc',ProductCreat.as_view(),name='pc'),
    path('pu/<int:pk>',ProductUpdate.as_view(),name='pu'),
    path('pd/<int:pk>/',ProductDetail.as_view(),name='pd'),
    path('del/<int:pk>/',ProducttDel.as_view(),name='del'),

    
]