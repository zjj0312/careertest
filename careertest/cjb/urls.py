"""careertest URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.conf.urls import url
from . import views


urlpatterns = [
    url('jobneed3/', views.jobneed3),
    url('jobneed2/', views.jobneed2),
    url('jobneed/', views.jobneed_query),
    url('jobneed_add/', views.jobneed_add),
    url('jobneed_edit/', views.jobneed_edit),
    url('jobneed_del/', views.jobneed_del),
    url('tester/', views.tester_query),
    url('tester_add/', views.tester_add),
    url('tester_edit/', views.tester_edit),
    url('tester_del/', views.tester_del),
    url('company/', views.company),
    url('main/', views.main),
    url('login/', views.login)
]
