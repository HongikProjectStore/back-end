from django.db import models

# Create your models here.

class Product(models.Model):
    pid = models.AutoField(primary_key=True)  # positive int
    name = models.CharField(max_length=50)
    kinds = models.IntegerField(null=True)   # enum type
    manufacturer = models.CharField(max_length=20)
    price = models.IntegerField()
    product_img_url = models.URLField(max_length=200, default="http://www.bizforms.co.kr/form/image/thumb_ing.gif")
    convenience_store = models.CharField(max_length=50, null=True)
    event_type = models.JSONField(max_length=50, null=True)