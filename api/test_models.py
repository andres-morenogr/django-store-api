from django.test import TestCase
from .models import Seller


class SellerTest(TestCase):
    """ Test module for Seller model """

    def setUp(self):
        Seller.objects.create(
            name='Django', logo='logo')

    def test_Schema(self):
        seller = Seller.objects.get(name='Django')
        self.assertEqual(seller.name, 'Django')
