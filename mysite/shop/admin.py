from django.contrib import admin

from .models import Product


@admin.register(Product)  # Регистрация модели Product в административной панели.
class ProductAdmin(admin.ModelAdmin):
    """
    Административная панель для модели Product.
    """
    list_display = ['pk', 'name', 'description_repr', 'price', 'discount',
                    'created_dat']  # Список полей выводимых в административную панель.
    list_display_links = ['pk',
                          'name']  # Поля, которые будут использоваться для создания ссылки в административной панели.
    ordering = ['pk', 'price', 'created_dat', 'name']  # Порядок сортировки в административной панели умолчанию.
    search_fields = 'name', 'description'  # Поля, по которым можно осуществлять поиск в административной панели.'

    def description_repr(self, obj: Product) -> str:
        return obj.description[:50]  # переопределение вывода поля description в административной панели.

    # admin.site.register(Product, ProductAdmin)  # Вариант опеределения модели Product в административной панели.
