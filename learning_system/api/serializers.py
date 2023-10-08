from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Product, Lesson, UserData, Probe


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username',]


class ProductSerializer(serializers.ModelSerializer):
    owner = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Product
        fields = ['id', 'title', 'owner']


class LessonSerializer(serializers.ModelSerializer):
    product = serializers.ReadOnlyField(source='product.title')

    class Meta:
        model = Lesson
        fields = ['id', 'title', 'product', 'url', 'time']


class UserDataSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    lesson = serializers.ReadOnlyField(source='lesson.title')

    class Meta:
        model = UserData
        fields = ['id', 'user', 'lesson', 'status', 'timecode']


# class ProbeSerializer(serializers.Serializer):
#     """Попытка серилизовать данные об уроках пользователя"""
#     lesson = serializers.CharField(max_length=200)
#     user = serializers.CharField(max_length=200)
#     status = serializers.BooleanField()
#     timecode =serializers.IntegerField()
#
#     def create(self, validated_data):
#         return Probe.objects.create(**validated_data)
