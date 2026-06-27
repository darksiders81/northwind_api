from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import UsStates
from .serializers import UsStatesSerializer


class UsStatesModelViewSet(viewsets.ModelViewSet):
    serializer_class = UsStatesSerializer
    queryset = UsStates.objects.all()