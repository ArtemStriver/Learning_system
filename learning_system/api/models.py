from django.db import models
from django.contrib.auth.models import User


class Product(models.Model):
    """Модель Продукта и их владельца"""
    title = models.CharField(max_length=200)
    owner = models.ManyToManyField(User, related_name='product_owner', )

    class Meta:
        ordering  = ('title', )

    def __str__(self):
        return self.title


class Lesson(models.Model):
    """Модель Урока и его данными, а также связью с Продуктом"""
    title = models.CharField(max_length=200)
    product = models.ForeignKey(Product, related_name='lesson', on_delete=models.CASCADE)
    url = models.URLField()
    time = models.IntegerField()

    class Meta:
        ordering  = ('title', )

    def __str__(self):
        return self.title


class UserData(models.Model):
    """Модель Данных пользователя, содержит данные о статусе и времени просмотра урока пользователем"""
    title = models.CharField(max_length=200)
    user = models.ForeignKey(User, related_name='user_to_lesson', on_delete=models.CASCADE)
    lesson = models.ForeignKey(Lesson, related_name='lessons_to_user', on_delete=models.CASCADE)
    status = models.BooleanField()
    timecode = models.IntegerField()

    class Meta:
        ordering = ('title',)

    def __str__(self):
        return self.title


# class Probe(models.Model):
#     """Попытка организовать вывод данных о всех уроках пользователя"""
#     lesson = models.CharField(max_length=200)
#     user = models.CharField(max_length=200)
#     status = models.BooleanField()
#     timecode =models.IntegerField()
