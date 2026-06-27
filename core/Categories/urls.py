from django.urls import path
from .views import CategoryModelViewSet
from rest_framework.routers import DefaultRouter




router = DefaultRouter()

router.register('category', CategoryModelViewSet, basename='category')


urlpatterns = router.urls