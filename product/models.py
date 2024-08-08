from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField()
    price = models.FloatField()
    quantity = models.IntegerField()

    def __str__(self):
        return self.name