from django.contrib import admin
from .models import TweetModel,TweetComment

# Register your models here.
#TweetModel을 admin에 등록해주겠다.
admin.site.register(TweetModel)

