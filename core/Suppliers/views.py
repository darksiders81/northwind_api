from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import Suppliers
from .serializers import SuppliersSerializer


class SuppliersModelViewSet(viewsets.ModelViewSet):
    serializer_class = SuppliersSerializer
    queryset = Suppliers.objects.all()
