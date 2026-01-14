from django.core.management import BaseCommand

from shopapp.models import Product


class Command(BaseCommand):
    """
    Command to create products
    """

    def handle(self, *args, **options):
        self.stdout.write('Creating products...')

        products = [
            'Laptop',
            'Descktop',
            'Smartphone',
        ]

        # product = Product(name='Laptop')
        # product.save()

        for product in products:
            product, created = Product.objects.get_or_create(name=product)
            self.stdout.write(self.style.SUCCESS(f'Product {product.name} created  - {created}'))