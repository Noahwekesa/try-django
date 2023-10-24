from django.db import models

# Create your models here.
class product(models.Model):
    title                 = models.CharField(max_length=150)
    descriotion   = models.TextField(blank=False, null=True)
    price              = models.DecimalField(max_digits=10000, decimal_places=2)
    summary      = models.TextField(default="just learning")
