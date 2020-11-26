from django.db import models

# Create your models here.

class Test(models.Model):
    value = models.CharField(max_length=60, default='') 
    
    def __str__(self):
        return self.value
