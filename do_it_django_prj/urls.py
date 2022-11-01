"""do_it_django_prj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path,include # include 다른데 있는 url 불러다 쓰겠다

urlpatterns = [
    path("blog/",include('blog.urls')), # 블로그 폴더 안의 urls로 가라
    path("admin/", admin.site.urls),
    path("",include('single_pages.urls')), # single_pages.url에 파일만들어야함
] # 나머지는 site쪽에 urls있음??
