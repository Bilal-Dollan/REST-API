from django.db import models


class Product(models.Model):
    title = models.CharField(max_length=128)
    content = models.TextField(blank=True)
    price = models.DecimalField(max_digits=15, decimal_places=2)
