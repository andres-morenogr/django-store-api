from django.db import models

# modelo vendedor
class Seller(models.Model):
    name = models.CharField(max_length=100)
    logo = models.URLField(max_length = 200)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'sellers'
        verbose_name = 'Seller'
        verbose_name_plural = 'Sellers'
        ordering = ['id']

# modelo ciudad
class City(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=10)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'cities'
        verbose_name = 'City'
        verbose_name_plural = 'Cities'
        ordering = ['id']


# modelo item
class Item(models.Model):
    name = models.CharField(max_length=300)
    brand = models.CharField(max_length=300)
    thumbnail = models.URLField(max_length = 200)
    images = ArrayField(models.URLField(max_length = 200))
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE)
    detail = models.TextField(max_length=1000, verbose_name='Información del item')
    price = models.FloatField()
    currency = models.CharField(max_length=5)
    

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'items'
        verbose_name = 'Item'
        verbose_name_plural = 'Items'
        ordering = ['id']
