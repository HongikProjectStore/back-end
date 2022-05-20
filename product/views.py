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

# request 1 product
@api_view(["GET"])
def getProduct(request):
    # product = Product.objects.all()
    product = [
        {
            "pid": 1,
            "name": "test1",
            "kinds": 1,
            "price": 10000,
            "product_img_url": "https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.istockphoto.com%2Fphotos%2Ffree&psig=AOvVaw31ul-Ovxm050aGK6E65h3D&ust=1653047632042000&source=images&cd=vfe&ved=0CAwQjRxqFwoTCIC_2rrA6_cCFQAAAAAdAAAAABAD",
            "convenience_store": "CU/GS25",
            "event_type": "1+1/2+1",
        }
    ]
    serializer = ProductSerializer(product, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


# request n products
@api_view(["GET"])
def getProductList(request, num):
    product_list = []
    for i in num:
        product = dict(
            pid=i,
            names="test" + str(i),
            kinds=i % 10,
            price=i * 1000,
            product_img_url="https://www.google.com/url?sa=i&url=http%3A%2F%2Fbizshop.bizforms.co.kr%2Fshop%2Fproduct_view%2Fbiz_soft142018673129.asp&psig=AOvVaw2tSCD8_wq1lFHnsSDbe8DU&ust=1653148457888000&source=images&cd=vfe&ved=0CAwQjRxqFwoTCJDCg4m47vcCFQAAAAAdAAAAABAJ",
            convenience_store="CU/GS25/ºº∫Ï¿œ∑π∫Ï/Emart24",
            event_type="1+1/2+1/«“¿Œ/æ¯¿Ω",
        )
        product_list.append(product)

    serializer = ProductSerializer(product_list, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)
