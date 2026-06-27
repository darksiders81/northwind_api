from django.shortcuts import render
from rest_framework import viewsets
from .serializers import CategoriesSerializer
from .models import Categories
# Create your views here.



class CategoryModelViewSet(viewsets.ModelViewSet):
    serializer_class = CategoriesSerializer
    queryset = Categories.objects.all()