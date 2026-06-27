from rest_framework.routers import DefaultRouter
from .views import UsStatesModelViewSet

router = DefaultRouter()

router.register("us-states", UsStatesModelViewSet, basename="us-states")

urlpatterns = router.urls
