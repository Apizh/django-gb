from django.db import models
from django.contrib.auth.models import User


class Product(models.Model):
    """
    Класс модели для представления продукта.
    """

    class Meta:
        ordering = ['price']  # Сортировка продуктов по цене

    name = models.CharField(max_length=100)  # Название продукта, с максимальной длиной в 100 символов
    description = models.TextField(null=False, blank=True)  # Описание продукта
    price = models.DecimalField(max_digits=8, decimal_places=2,
                                default=0)  # Цена продукта, с двумя знаками после запятой
    discount = models.SmallIntegerField(default=0)  # Скидка на продукт, в процентах
    created_dat = models.DateTimeField(auto_now_add=True)  # Дата и время создания продукта
    archived = models.BooleanField(default=False)  # Флаг архивирования продукта

    # @property
    # def description_repr(self) -> str:
    #     return self.description[:50] + '...'  # Обрезка текста описания до 50 символов

    def __str__(self) -> str:
        return f"Product(pk={self.pk}, name={self.name!r})"  # Переопределение отображение продукта в "админке"


class Order(models.Model):
    """
    Класс модели для представления заказа.
    """
    delivery_address = models.TextField(null=False, blank=True)  # Адрес доставки
    promocode = models.CharField(max_length=20, null=False, blank=True)  # Промокод
    created_at = models.DateTimeField(auto_now_add=True)  # Дата и время создания заказа
    user = models.ForeignKey(User, on_delete=models.PROTECT)  # Пользователь, сделавший заказ
    products = models.ManyToManyField(Product, related_name='orders')  # Продукты в заказе'
