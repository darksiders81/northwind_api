from rest_framework.routers import DefaultRouter
from .views import OrdersModelViewSet, OrderDetailsModelViewSet

router = DefaultRouter()

router.register("orders", OrdersModelViewSet, basename="orders")
router.register("order-details", OrderDetailsModelViewSet, basename="order-details")

urlpatterns = router.urls
