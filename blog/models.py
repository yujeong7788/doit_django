from django.db import models

# Create your models here.

class Post(models.Model): # 위에있는 모델 상속받음 부모 기본 정보 받음
    title = models.CharField(max_length=30) # 프라이머리는 자동으로 생성 , charfield 한줄짜리 문자 필드, 짧은글
    content = models.TextField() # 텍스트 어레이와 연결된다. 더 많은 데이터 받을 수 있음, 긴글

    create_at = models.DateTimeField(auto_now_add=True) # 날짜 시간 처음 만들어진거 자동으로 추가
    update_at = models.DateTimeField(auto_now=True) # 수정시간 자동으로
    # author : 추후 작성 예정
    # 필드 바뀌었으니 미그레이션
    
    def __str__(self): # 부모가 가지고있는거라 똑같이 , self 넣는 이유는 뭘까?
        return f'[{self.id}] {self.title}' # 함수가 추가된거라서 migrate 필요없음
    