from django.core.management.base import BaseCommand
from hw2_shop_app.models import Client


class Command(BaseCommand):
    help = "update phone client by id client"

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='client id')  # pk - id
        parser.add_argument("phone", type=str, help="phone client")

    def handle(self, *args, **kwargs):
        pk = kwargs.get('pk')
        phone = kwargs.get('phone')
        client = Client.objects.filter(pk=pk).first()  # поиск строки по id
        client.phone_number = phone
        client.save()  # сохранение в БД
        self.stdout.write(f'{client}')
