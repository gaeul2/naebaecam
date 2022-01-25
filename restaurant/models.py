# restaurant/models.py
from django.db import models


# Create your models here. 새로 모델만들면 python manage.py makemigrations, python manage.py migrate 해줘야한다

class MyTopping(models.Model):
    class Meta:
        db_table = "my_topping"

    def __str__(self):
        return self.topping_name

    topping_name = models.CharField(max_length=100)


class MyPizza(models.Model):
    class Meta:
        db_table = "my_pizza"

    def __str__(self):
        return self.pizza_name

    pizza_name = models.CharField(max_length=100)
    pizza_topping = models.ManyToManyField(MyTopping)
    #my_pizza_pizza_topping 이 manytomany로 생긴듯