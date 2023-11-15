from django.db import models

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=100) # max_length always required when using charfield
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(decimal_places=2, max_digits=1000)
    summary = models.TextField(blank=False, null=True)
    featured = models.BooleanField(default=True)