from django.core.management.base import BaseCommand
from hw2_shop_app.models import Product


class Command(BaseCommand):
    help = "update product cost by id product"

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='id of products')  # pk - id
        parser.add_argument("cost", type=float, help="price of product")

    def handle(self, *args, **kwargs):
        pk = kwargs.get('pk')
        cost = kwargs.get('cost')
        product = Product.objects.filter(pk=pk).first()  # поиск строки по id
        product.cost = cost
        product.save()  # сохранение в БД
        self.stdout.write(f'{product}')
