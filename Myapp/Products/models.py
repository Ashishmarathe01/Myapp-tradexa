from django.db import models

# Create your models here.
class Product(models.Model):
    name=models.CharField(max_length=50)
    weight=models.DecimalField(max_digits=3,decimal_places=1)
    price=models.IntegerField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

