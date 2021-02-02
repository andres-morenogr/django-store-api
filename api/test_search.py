from django.test import TestCase
from .models import Seller


class ViewsTestCase(TestCase):

    def setUp(self):
        Seller.objects.create(
            name='Django', logo='logo')

    def test_index_loads_properly(self):  # Arrange
        """The index page loads properly"""
        response = self.client.get('http://localhost:8000/django_api/')  # Act
        self.assertEqual(response.status_code, 200)  # Assert

    def test_search(self):  # Arrange
        """The index page loads properly"""
        response = self.client.get(
            'http://localhost:8000/django_api/search/?q=computador')  # Act
        self.assertEqual(response.status_code, 200)  # Assert
        self.assertEqual(response.data['total'], 0)  # Assert
