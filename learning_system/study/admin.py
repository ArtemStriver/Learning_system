from django.contrib import admin

from study.models import Lesson, LessonViewInfo


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    pass


@admin.register(LessonViewInfo)
class LessonViewInfoAdmin(admin.ModelAdmin):
    pass
