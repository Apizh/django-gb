from django.contrib import admin

from .models import Product


class ProductAdmin(admin.ModelAdmin):
    """
    Административная панель для модели Product.
    """
    list_display = ['pk', 'name', 'description', 'price', 'discount',
                    'created_dat']  # Список полей выводимых в административную панель.
    list_display_links = ['pk',
                          'name']  # Поля, которые будут использоваться для создания ссылки в административной панели.


admin.site.register(Product, ProductAdmin)  # Опеределение модели Product в административной панели.
