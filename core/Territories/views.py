from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import Region, Territories
from .serializers import RegionSerializer, TerritoriesSerializer


class RegionModelViewSet(viewsets.ModelViewSet):
    serializer_class = RegionSerializer
    queryset = Region.objects.all()


class TerritoriesModelViewSet(viewsets.ModelViewSet):
    serializer_class = TerritoriesSerializer
    queryset = Territories.objects.select_related('region').all()