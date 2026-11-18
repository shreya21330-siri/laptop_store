from django.db import models


class Laptop(models.Model):
    name = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    image = models.CharField(max_length=10000)
    
    def __str__(self):
        return self.name

# Create your models here.
