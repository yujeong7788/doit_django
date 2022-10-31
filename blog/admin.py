from django.contrib import admin
from .models import Post # 현재경로에 넣어줌
# Register your models here.
admin.site.register(Post)
