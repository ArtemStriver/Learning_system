from datetime import datetime

from django.contrib.auth.models import User
from django.db import models

from catalog.models import Product

"""
Модель урока и модель информации об уроке для конкретного пользователя.
"""


class Lesson(models.Model):
    title = models.CharField(max_length=32)
    video_url = models.URLField()
    video_duration = models.IntegerField(default=0)
    products = models.ManyToManyField(Product)


class LessonStatusEnum(models.TextChoices):
    """Класс для отображения информации о статусе просмотра урока."""
    VIEWED = 'VIEWED'
    NOT_VIEWED = 'N0T_VIEWED'


class LessonViewInfo(models.Model):
    lesson = models.ForeignKey(Lesson, models.CASCADE, related_name='views')
    user = models.ForeignKey(User, models.CASCADE)
    status = models.CharField(choices=LessonStatusEnum.choices, default=LessonStatusEnum.NOT_VIEWED, max_length=32)
    view_time = models.IntegerField(default=0)
    last_view_datetime = models.DateTimeField(default=datetime.now())

    class Meta:
        unique_together = ('lesson', 'user')
