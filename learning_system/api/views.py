from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView

from . import serializers
from django.contrib.auth.models import User
from .models import Product, Lesson, UserData
from .serializers import ProductSerializer, LessonSerializer, UserDataSerializer


class UserList(generics.ListAPIView):
    """Отображение таблице с данными о пользователе через REST"""
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer


class GetProductInfoView(APIView):
    """Отображение таблице Product через REST"""
    def get(self, request):
        queryset = Product.objects.all()
        serializer_for_queryset = ProductSerializer(
            instance=queryset,
            many=True
        )
        return Response(serializer_for_queryset.data)


class GetLessonInfoView(APIView):
    """Отображение таблице Lesson через REST"""
    def get(self, request):
        queryset = Lesson.objects.all()
        serializer_for_queryset = LessonSerializer(
            instance=queryset,
            many=True
        )
        return Response(serializer_for_queryset.data)


class GetUserDataInfoView(APIView):
    """Отображение таблице UserData через REST"""
    def get(self, request):
        queryset = UserData.objects.all()
        serializer_for_queryset = UserDataSerializer(
            instance=queryset,
            many=True
        )
        return Response(serializer_for_queryset.data)


# class Probe(APIView):
#     """Попытка отобразить список всех уроков пользователя через REST"""
#     def get(self, request, user_id=1):
#         alluserproducts = Product.objects.all() #filter(id=user_id)
#         for product in alluserproducts:
#             alluserlessens = Lesson.objects.all()
#             userdata = UserData.objects.get(id=1)
#             Probe(lesson=alluserlessens[1].title, user=product.owner, status=userdata.status, timecode=userdata.timecode)
#         serializer = ProbeSerializer()
#         return Response(serializer.data)
