from sys import api_version
from xmlrpc.client import APPLICATION_ERROR
from django.shortcuts import render
from rest_framework import viewsets, permissions, generics, status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.generics import get_object_or_404 
from .models import Product
from .serializers import ProductSerializer
# Create your views here.

@api_view(['GET'])
def getProduct(request):
     # product = Product.objects.all()

    product = [{'pid' : 1, 'name' : "테스트", 'kinds' : "noodles", 'price' : 10000, 'product_img_url' : "https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.istockphoto.com%2Fphotos%2Ffree&psig=AOvVaw31ul-Ovxm050aGK6E65h3D&ust=1653047632042000&source=images&cd=vfe&ved=0CAwQjRxqFwoTCIC_2rrA6_cCFQAAAAAdAAAAABAD",
    'convenience_store': "CU/GS25", 'event_type' : '1+1/2+1'}]
    serializer = ProductSerializer(product, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)
