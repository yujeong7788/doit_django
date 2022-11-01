from urllib.parse import urlparse
from django.urls import path
from . import views

urlpatterns = [
    path('',views.landing), #'' 현재경로, views landing 함수에서 처리
    path('about_me/',views.about_me), # about_me 함수에서 처리
]
