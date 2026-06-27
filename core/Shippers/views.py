from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import Shippers
from .serializers import ShippersSerializer


class ShippersModelViewSet(viewsets.ModelViewSet):
    serializer_class = ShippersSerializer
    queryset = Shippers.objects.all()