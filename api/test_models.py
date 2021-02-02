from django.test import TestCase
from .models import Seller, Item


class SellerTest(TestCase):
    """ Test module for Seller model """

    def setUp(self):
        Seller.objects.create(
            name='Django', logo='logo')

    def test_Schema(self):
        seller = Seller.objects.get(name='Django')
        self.assertEqual(seller.name, 'Django')


class ItemTest(TestCase):
    """ Test module for Item model """

    def setUp(self):
        Item.objects.create(name='computador',
                            thumbnail='http://mco-s2-p.mlstatic.com/690248-MCO42347578960_062020-I.jpg',
                            pictures=[
                                 'http://mco-s2-p.mlstatic.com/690248-MCO42347578960_062020-O.jpg'],
                            price=3299000,
                            brand='Lenovo',
                            description='Aio Lenovo I5 8gb 1tb+128 Ssd  Ideacentre A340 White 23.8 ',
                            currency='COP',
                            rating=4,
                            city="('name', 'Bogotá'), ('code', 'BOG')",
                            seller={
                                 "id": 5,
                                 "name": "django_api",
                                 "logo": "https://www.django-rest-framework.org/img/logo.png"
                            }
                            )

    def test_Schema_name(self):
        item = Item.objects.get(name='computador')
        self.assertEqual(item.name, 'computador')
