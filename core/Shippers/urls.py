from rest_framework.routers import DefaultRouter
from .views import ShippersModelViewSet

router = DefaultRouter()

router.register('shippers', ShippersModelViewSet, basename='shippers')

urlpatterns = router.urls