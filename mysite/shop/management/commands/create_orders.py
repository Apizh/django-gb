from django.core.management import BaseCommand
from django.contrib.auth.models import User
from shop.models import Order


class Command(BaseCommand):
    """
    Создаём заказы в БД.
    """

    def handle(self, *args, **options):
        self.stdout.write("Creating orders...\n")
        user = User.objects.get(username='admin')
        order = Order.objects.get_or_create(
            delivery_address='ул. Пушкина, д. 19',
            promocode='promocode',
            user=user
        )

        self.stdout.write(f"Создан заказ: {order}\n")
