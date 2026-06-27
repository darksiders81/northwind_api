from rest_framework import serializers
from .models import Employees, EmployeeTerritories


class EmployeesSerializer(serializers.ModelSerializer):
    # self-referential فیلد برای نمایش مدیر
    reports_to_name = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Employees
        fields = [
            'employee_id',
            'last_name',
            'first_name',
            'title',
            'title_of_courtesy',
            'birth_date',
            'hire_date',
            'address',
            'city',
            'region',
            'postal_code',
            'country',
            'home_phone',
            'extension',
            'notes',
            'photo_path',
            'reports_to',
            'reports_to_name',
            # photo حذف شد چون binary هست
        ]

    def get_reports_to_name(self, obj):
        if obj.reports_to:
            return f"{obj.reports_to.first_name} {obj.reports_to.last_name}"
        return None


class EmployeeTerritoriesSerializer(serializers.ModelSerializer):
    employee = EmployeesSerializer(read_only=True)

    employee_id = serializers.IntegerField(write_only=True)
    territory_id = serializers.CharField(write_only=True)

    class Meta:
        model = EmployeeTerritories
        fields = [
            'employee',
            'employee_id',
            'territory_id',
        ]