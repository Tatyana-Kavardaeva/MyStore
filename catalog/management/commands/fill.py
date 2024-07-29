import json
from django.core.management.base import BaseCommand
from catalog.models import Category, Product


class Command(BaseCommand):

    @staticmethod
    def json_read_categories():
        with open('catalog.json', 'r', encoding='utf-8') as f:
            data = json.load(f)
            categories = []
            for items in data:
                if items.get('model') == 'catalog.category':
                    categories.append(items)
        return categories

    @staticmethod
    def json_read_products():
        with open('catalog.json', 'r', encoding='utf-8') as f:
            data = json.load(f)
            products = []
            for items in data:
                if items.get('model') == 'catalog.product':
                    products.append(items)
        return products

    def handle(self, *args, **options):
        Product.objects.all().delete()
        Category.objects.all().delete()

        product_for_create = []
        category_for_create = []

        for categories in Command.json_read_categories():
            category = Category(
                name=categories['fields']['name'],
                description=categories['fields']['description']
            )
            category_for_create.append(category)

        Category.objects.bulk_create(category_for_create)

        for products in Command.json_read_products():
            try:
                category = Category.objects.get(id=products['fields']['category'])
            except Category.DoesNotExist:
                category = None

            product = Product(
                name=products['fields']['name'],
                description=products['fields']['description'],
                image=products['fields']['image'],
                category=category,
                price=products['fields']['price'],
                created_at=products['fields']['created_at'],
                updated_at=products['fields']['updated_at']
            )
            product_for_create.append(product)

        # Создаем продукты в базе
        Product.objects.bulk_create(product_for_create)

        self.stdout.write(self.style.SUCCESS('Data loaded successfully.'))
