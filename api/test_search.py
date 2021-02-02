from django.test import TestCase
from .models import Seller, Item


class ViewsTestCase(TestCase):

    def setUp(self):  # Arrange
        Seller.objects.create(
            name='Django', logo='logo')
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

    def test_response_status(self):
        """Status should be 200"""
        response = self.client.get(
            'http://localhost:8000/django_api/search/')  # Act
        self.assertEqual(response.status_code, 200)  # Assert

    def test_search_without_results(self):
        """Should not have items"""
        response = self.client.get(
            'http://localhost:8000/django_api/search/?q=asdfg')  # Act
        self.assertEqual(response.status_code, 200)  # Assert
        self.assertEqual(response.data['total'], 0)  # Assert

    def test_search_with_results(self):
        """Should  have items"""
        response = self.client.get(
            'http://localhost:8000/django_api/search/?q=computador')  # Act
        self.assertEqual(response.status_code, 200)  # Assert
        self.assertEqual(response.data['total'], 1)  # Assert
