from pyexpat import model
from django.db import models
from enum import Enum

# Create your models here.
class ProductType(Enum):
    BEVERAGE = 0
    DAIRY_PRODUCT = 1
    SNACK = 2
    FOOD = 3
    SUGARS = 4
    BAKERY = 5
    NOODLE = 6
    ICECREAM = 7
    DAIRY_NECCESITY = 8
    ETC = 9


class Product(models.Model):
    pid = models.PositiveIntegerField(primary_key=True)  # positive int
    name = models.CharField(max_length=50)
    kinds = models.PositiveSmallIntegerField()  # enum type
    price = models.PositiveIntegerField()
    product_img_url = models.CharField(max_length=200)
    convenience_store = models.CharField(max_length=50)
    event_type = models.CharField(max_length=50)
