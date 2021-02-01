from django.test import TestCase

class ViewsTestCase(TestCase):

    def test_index_loads_properly(self): # Arrange
        """The index page loads properly"""
        response = self.client.get('http://localhost:8000/django_api/') # Act
        self.assertEqual(response.status_code, 200) # Assert
