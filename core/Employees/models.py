from django.db import models


# Create your models here.
class EmployeeTerritories(models.Model):
    pk = models.CompositePrimaryKey("employee_id", "territory_id")
    employee = models.ForeignKey("Employees", models.DO_NOTHING)
    territory = models.ForeignKey("Territories.Territories", models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = "employee_territories"


class Employees(models.Model):
    employee_id = models.SmallIntegerField(primary_key=True)
    last_name = models.CharField(max_length=20)
    first_name = models.CharField(max_length=10)
    title = models.CharField(max_length=30, blank=True, null=True)
    title_of_courtesy = models.CharField(max_length=25, blank=True, null=True)
    birth_date = models.DateField(blank=True, null=True)
    hire_date = models.DateField(blank=True, null=True)
    address = models.CharField(max_length=60, blank=True, null=True)
    city = models.CharField(max_length=15, blank=True, null=True)
    region = models.CharField(max_length=15, blank=True, null=True)
    postal_code = models.CharField(max_length=10, blank=True, null=True)
    country = models.CharField(max_length=15, blank=True, null=True)
    home_phone = models.CharField(max_length=24, blank=True, null=True)
    extension = models.CharField(max_length=4, blank=True, null=True)
    photo = models.BinaryField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    reports_to = models.ForeignKey(
        "self", models.DO_NOTHING, db_column="reports_to", blank=True, null=True
    )
    photo_path = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = "employees"
