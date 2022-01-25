from django.contrib import admin
from .models import MyPizza, MyTopping

# Register your models here. 여기에 모델들 등록

admin.site.register(MyPizza)
admin.site.register(MyTopping)