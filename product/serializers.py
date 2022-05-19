from itertools import product
from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['pid', 'name','kinds', 'price','product_img_url','convenience_store','event_type']

