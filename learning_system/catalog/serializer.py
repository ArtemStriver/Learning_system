from rest_framework import serializers

"""
Сериализатор для отображения статистики по продукту.
"""


class ProductStatisticSerializer(serializers.Serializer):
    title = serializers.CharField()
    lesson_view_count = serializers.IntegerField()
    total_view_time = serializers.IntegerField()
    total_users_on_product = serializers.IntegerField()
    purchasing_percent = serializers.FloatField()
