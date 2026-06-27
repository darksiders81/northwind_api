from rest_framework.routers import DefaultRouter
from .views import EmployeesModelViewSet, EmployeeTerritoriesModelViewSet

router = DefaultRouter()

router.register("employees", EmployeesModelViewSet, basename="employees")
router.register(
    "employee-territories",
    EmployeeTerritoriesModelViewSet,
    basename="employee-territories",
)

urlpatterns = router.urls
