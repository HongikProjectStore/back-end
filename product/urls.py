from django.urls import path, include
from .views import getProduct

urlpatterns = [
    path("", getProduct),
]
