from django.contrib import admin #장고에서 admin툴을 사용하겠다.
#동일한 폴더내의 model을 불러오겠다. models.py의 UserModel을 가져오겠다.
from .models import UserModel #우리가 생성한 모델을 가져오는것.

# Register your models here.
#우리가 가져온 UserModel을 관리자 계정에, 관리자 페이지에 넣어주겠다.
admin.site.register(UserModel) # 이 코드가 나의 UserModel을 Admin에 추가 해 줍니다