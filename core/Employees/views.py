from rest_framework import viewsets
from .models import Employees, EmployeeTerritories
from .serializers import EmployeesSerializer, EmployeeTerritoriesSerializer


class EmployeesModelViewSet(viewsets.ModelViewSet):
    serializer_class = EmployeesSerializer
    queryset = Employees.objects.select_related('reports_to').all()


class EmployeeTerritoriesModelViewSet(viewsets.ModelViewSet):
    serializer_class = EmployeeTerritoriesSerializer
    queryset = EmployeeTerritories.objects.select_related('employee', 'territory').all()