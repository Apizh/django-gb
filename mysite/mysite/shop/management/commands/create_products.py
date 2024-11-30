from django.core.management import BaseCommand

from shop.models import Product


class Command(BaseCommand):
    """
    Создаём новые продукты в БД.
    """
    def handle(self, *args, **options):
        self.stdout.write('Создаем новые продукты в БД...')
        products = [
            'Apple',
            'Banana',
            'Orange',
            'Pear',
            'Grape',
            'Strawberry',
        ]
        for product in products:
            # Добавляем продукты в БД
            product, created = Product.objects.get_or_create(name=product, description='Описание продукта' + product)
            self.stdout.write(f"Добавлен продукт :{product.name}")
            # Ваша реализация здесь

        self.stdout.write(self.style.SUCCESS('Создаем новые ...'))