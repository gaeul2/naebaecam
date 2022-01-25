# tweet/models.py
from django.db import models
#user앱의 model.py에서 UserModel을 불러왔다
from user.models import UserModel
from taggit.managers import TaggableManager


# Create your models here.
class TweetModel(models.Model):
    class Meta:
        db_table = "tweet"
              #ForeignKey가 특징! 다른 데이터베이스에서 내용을 가져오겠다.
              #다른 모델을 갖고와서 여기안에 넣어놓겠다!
        #author는 UserModel을 참조하는 외래키이기 때문에 UserModel과 일치하는 모든 정보를 가져옴.
    author = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    content = models.CharField(max_length=256)
    tags = TaggableManager(blank=True)#비어있어도 괜찮다
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class TweetComment(models.Model): #댓글들을 저장할 모델을 생성
    class Meta:
        db_table = "comment" #comment라는 db테이블을 만들어줘
        #트윗은 TweetModel에 있으니까 외래키로 참조
    tweet = models.ForeignKey(TweetModel, on_delete=models.CASCADE)
    author = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    comment = models.CharField(max_length=256)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    #모델 생성했으면 장고에 꼭 알려주는거 잊지마!
    #python manage.py makemigrations
    #python manage.py migrate




