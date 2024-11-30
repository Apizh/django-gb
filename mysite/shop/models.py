from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=100)  # Название продукта, с максимальной длиной в 100 символов
    description = models.TextField(null=False, blank=True)  # Описание продукта
