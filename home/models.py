from django.db import models

# Create your models here.

class Product(models.Model):
    title=models.CharField(max_length=60)
    description=models.TextField(blank=True,null=True)
    price=models.FloatField(default=0)
