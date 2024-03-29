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
from django.urls import path
from . import views # 현재 폴더에 있는 view를 임포트해라

urlpatterns = [
    path('',views.index),
    path('<int:pk>/',views.single_post_page), # int:pk 일때 views ~~ 함수가서 처리
    
] # path('',views.index) 블로그에 들어오면 view.index로 보내라 '' > /blog/

