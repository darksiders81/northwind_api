from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import Orders, OrderDetails
from .serializers import OrdersSerializer, OrderDetailsSerializer


class OrdersModelViewSet(viewsets.ModelViewSet):
    serializer_class = OrdersSerializer
    queryset = (
        Orders.objects.select_related("customer", "employee", "ship_via")
        .prefetch_related("orderdetails_set")
        .all()
    )


class OrderDetailsModelViewSet(viewsets.ModelViewSet):
    serializer_class = OrderDetailsSerializer
    queryset = OrderDetails.objects.select_related("order", "product").all()
