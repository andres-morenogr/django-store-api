from django.db import models
from jsonfield import JSONField

# Seller
class Seller(models.Model):
    name = models.CharField(max_length=50)
    data = JSONField()

    def __str__(self):
        return self.name

# Item
class Item(models.Model):
    name = models.CharField(max_length=50)
    data = JSONField()

    def __str__(self):
        return self.name
