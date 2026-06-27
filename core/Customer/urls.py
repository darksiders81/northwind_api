from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import (
    CustomerDemographicsModelViewSet,
    CustomerCustomerDemoModelViewSet,
    CustomerModelViewSet,
)

router = DefaultRouter()

router.register("customers", CustomerModelViewSet, basename="customers")
router.register(
    "customer-demographics",
    CustomerDemographicsModelViewSet,
    basename="customer-demographics",
)
router.register(
    "customer-demo", CustomerCustomerDemoModelViewSet, basename="customer-demo"
)

urlpatterns = router.urls
