from pyexpat import model
from django.db import models

# Create your models here.

class Product(models.Model):
    pid = models.PositiveIntegerField(primary_key=True) # Inter크기
    name = models.CharField(max_length=50)
    kinds = models.CharField(max_length=50)
    price = models.PositiveIntegerField()
    product_img_url = models.CharField(max_length=200)
    convenience_store =models.CharField(max_length=50)
    event_type = models.CharField(max_length=50) 
    


