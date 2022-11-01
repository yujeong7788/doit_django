from django.shortcuts import render # render template 과 같은 역할
from .models import Post
# Create your views here.

def index(request): # 함수쪽에 무조건 request 입력
    posts = Post.objects.all().order_by('-id') # post 테이블 object 데이터를 다 들고오겠다, order_by 정렬 -붙이면 디센딩(최근글이 먼저 옴), id, pk 모두 가능
    return render(
        request, # 적어줘야함
        'blog/index.html',# 블로그 파일 만들고 인덱스.html 넣어주겠다.
        {
            'posts':posts,
        }
    ) 
    
def single_post_page(request,pk): #???
    post = Post.objects.get(pk=pk) # 하나만 가져오니까 
    return render(
        request,
        'blog/single_post_page.html', # html
        {
            'post':post,
        }
    )

    