from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import Products
from .serializers import ProductsSerializer


class ProductsModelViewSet(viewsets.ModelViewSet):
    serializer_class = ProductsSerializer
    queryset = Products.objects.select_related("category", "supplier").all()
