from django.contrib.auth.models import User
from django.db import models

"""
Модель продукта и модель доступа к продукту.
"""


class Product(models.Model):
    title = models.CharField(max_length=32)
    user = models.ForeignKey(User, models.PROTECT)


class ProductAccess(models.Model):
    user = models.ForeignKey(User, models.PROTECT)
    product = models.ForeignKey(Product, models.PROTECT, related_name='accesses')
    is_valid = models.BooleanField(default=True)
