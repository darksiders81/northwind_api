from rest_framework.routers import DefaultRouter
from .views import SuppliersModelViewSet

router = DefaultRouter()

router.register('suppliers', SuppliersModelViewSet, basename='suppliers')

urlpatterns = router.urls