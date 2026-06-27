from rest_framework.routers import DefaultRouter
from .views import ProductsModelViewSet

router = DefaultRouter()

router.register("products", ProductsModelViewSet, basename="products")

urlpatterns = router.urls
