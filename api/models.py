from django.db import models
#from django.contrib.postgres.fields import ArrayField

# modelo item
class Item(models.Model):
    name = models.CharField(max_length=300)
    brand = models.CharField(max_length=300)
    thumbnail = models.URLField(max_length = 200)
    pictures = models.CharField(max_length = 200)
    city = models.CharField(max_length = 200)
    seller = models.CharField(max_length = 200)
    description = models.TextField(max_length=1000, verbose_name='Información del item')
    price = models.FloatField()
    currency = models.CharField(max_length=5)
    rating = models.IntegerField()
    
    def __str__(self):
        return self.name

    class Meta:
        db_table = 'items'
        verbose_name = 'Item'
        verbose_name_plural = 'Items'
        ordering = ['id']
