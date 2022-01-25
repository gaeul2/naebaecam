#user/models.py
from django.db import models
#장고에서 사용하는 기본적인 모델을 사용하겠다.
from django.contrib.auth.models import AbstractUser
#장고가 관리하는 설정들에서 갖고오겠다.
from django.conf import settings

# Create your models here.
    #클래스의 이름 #models.Model클래스를 상속받겠다!. 그 기능들을 사용할수 있게됨
    #AbstractUser는 데이터베이스의 auth_user와 연동되는 클래스임
class UserModel(AbstractUser):
    class Meta:#DB 테이블의 이름을 지정해주는 정보. 데이터베이스에 정보를 넣어주는 역할을 하는친구
        db_table = "my_user" #내 db테이블이름이 = 'my_user'였으면 좋겠어!
                    #해당하는 정보들이 어떤형태로 들어갈지 설정

    #UserModel사용할건데 장고의 기본적인 모델을 사용하고 추가적으로 bio를 추가해줬다.
    bio = models.CharField(max_length=256, default='')  # 상태
    #모델을 수정했기때문에 장고에 알려줘야 되는데 일단 우리 프로젝트의 settings.py의 맨밑으로 가쟈

    #우리가 만든 AUTH_USER_MODEL을 UserModel가 참조하겠다.
    #follow필드안에 들어가는 정보들은 사용자정보다.
    #follow는 내가 팔로우하는 사람들. followee는 나를 팔로우하는 사람들
    follow = models.ManyToManyField(settings.AUTH_USER_MODEL,related_name='followee')



    #AbstractUser를 상속받을 때는 얘가 필요없음
    # username = models.CharField(max_length=20, null=False) #이름
    # password = models.CharField(max_length=256, null=False) #비밀번호
    # bio = models.CharField(max_length=256, default='')#상태
    # created_at = models.DateTimeField(auto_now_add=True)#생성일 이건 장고가 알아서 시간을 넣어줌
    # updated_at = models.DateTimeField(auto_now=True)#수정일


#model을 만들었다면
#1. 나 데이터베이스 만들었어/수정했어! 라고 알려줘야하고 (데이터베이스 변경을 알려줌)
#2. 그 데이터베이스 넣어줘!! (1번에서 만든거 적용해줘!!)