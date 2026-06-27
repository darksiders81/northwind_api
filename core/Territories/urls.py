from rest_framework.routers import DefaultRouter
from .views import RegionModelViewSet, TerritoriesModelViewSet

router = DefaultRouter()

router.register('regions', RegionModelViewSet, basename='regions')
router.register('territories', TerritoriesModelViewSet, basename='territories')

urlpatterns = router.urls