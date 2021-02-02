from django.test import TestCase
from .models import Seller, Item
from django.urls import reverse

class DetailViewTest(TestCase):

    def setUp(self):  # Arrange
        self.seller = Seller.objects.create(name='Django', logo='logo')
        self.item = Item.objects.create(
            _id=1,
            name='computador',
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

    def test_search_valid_item(self):
        """Get item with id"""
        #url = reverse('rest_framework:Item-detail', kwargs={'pk': '1'})
        url = 'http://localhost:8000/django_api/item/1/'

        response = self.client.get(url)  # Act
        self.assertEqual(response.status_code, 200)  # Assert
