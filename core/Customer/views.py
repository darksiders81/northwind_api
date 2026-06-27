from rest_framework import viewsets
from .models import CustomerCustomerDemo, CustomerDemographics, Customers
from .serializers import (
    CustomerDemographicsSerializer,
    CustomersSerializer,
    CustomerCustomerDemoSerializer,
)

# Create your views here.


class CustomerDemographicsModelViewSet(viewsets.ModelViewSet):
    serializer_class = CustomerDemographicsSerializer
    queryset = CustomerDemographics.objects.all()



class CustomerCustomerDemoModelViewSet(viewsets.ModelViewSet):
    serializer_class = CustomerCustomerDemoSerializer
    queryset = CustomerCustomerDemo.objects.all()


class CustomerModelViewSet(viewsets.ModelViewSet):
    serializer_class = CustomersSerializer
    queryset = Customers.objects.all()
