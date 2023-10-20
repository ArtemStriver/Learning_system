from django.db.models import Q, FilteredRelation, F
from rest_framework import viewsets, mixins, exceptions
from rest_framework.permissions import IsAuthenticated

from catalog.models import ProductAccess
from study.models import Lesson
from study.serializers import MyLessonsSerializer, MyLessonsByProductSerializer

"""
Представление данных о всех уроках по всем продуктам, к которым пользователь имеет доступ на основе ViewSet;
Представление данных о всех уроках конкретного продукта, к которым пользователь имеет доступ на основе ViewSet.
"""


def get_product_accesses(user):
    """Функция получения информации о наличии доступа к продукту у пользователя."""
    return ProductAccess.objects.filter(user=user, is_valid=True)


class MyLessonsViewSet(viewsets.GenericViewSet, mixins.ListModelMixin):
    serializer_class = MyLessonsSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        access = get_product_accesses(self.request.user)

        qs = Lesson.objects.filter(
            products__in=access.values('product_id')
        ).alias(
            view_info=FilteredRelation(
                'views',
                condition=Q(views__user=self.request.user)
            )
        ).annotate(
            status=F('view_info__status'),
            view_time=F('view_info__view_time')
        )

        return qs


class MyLessonsByProductViewSet(viewsets.GenericViewSet, mixins.ListModelMixin):
    serializer_class = MyLessonsByProductSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        product_id = self.kwargs['product_id']
        access = get_product_accesses(self.request.user)

        if not (product_id in access.values_list('product_id', flat=True)):
            raise exceptions.NotFound

        qs = Lesson.objects.filter(
            products=product_id
        ).alias(
            view_info=FilteredRelation(
                'views',
                condition=Q(views__user=self.request.user)
            )
        ).annotate(
            status=F('view_info__status'),
            view_time=F('view_info__view_time'),
            last_view_datetime=F('view_info__last_view_datetime')
        )

        return qs
