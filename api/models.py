from django.db import models
from jsonfield import JSONField

# Seller
class Seller(models.Model):
    name = JSONField()
    logo = JSONField()

    def __str__(self):
        return self.name

# Item
class Item(models.Model):
    _id = models.CharField(max_length=30)
    name = JSONField()
    thumbnail = JSONField()
    pictures = JSONField()
    price = JSONField()
    brand = JSONField()
    description = JSONField()
    currency = JSONField()
    rating = JSONField()
    city = JSONField()
    seller = JSONField()

    def __str__(self):
        return self.name
