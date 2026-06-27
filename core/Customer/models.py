from django.db import models

# Create your models here.


class CustomerCustomerDemo(models.Model):
    pk = models.CompositePrimaryKey("customer_id", "customer_type_id")
    customer = models.ForeignKey("Customers", models.DO_NOTHING)
    customer_type = models.ForeignKey("CustomerDemographics", models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = "customer_customer_demo"


class CustomerDemographics(models.Model):
    customer_type_id = models.CharField(primary_key=True, max_length=5)
    customer_desc = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "customer_demographics"


class Customers(models.Model):
    customer_id = models.CharField(primary_key=True, max_length=5)
    company_name = models.CharField(max_length=40)
    contact_name = models.CharField(max_length=30, blank=True, null=True)
    contact_title = models.CharField(max_length=30, blank=True, null=True)
    address = models.CharField(max_length=60, blank=True, null=True)
    city = models.CharField(max_length=15, blank=True, null=True)
    region = models.CharField(max_length=15, blank=True, null=True)
    postal_code = models.CharField(max_length=10, blank=True, null=True)
    country = models.CharField(max_length=15, blank=True, null=True)
    phone = models.CharField(max_length=24, blank=True, null=True)
    fax = models.CharField(max_length=24, blank=True, null=True)

    class Meta:
        managed = False
        db_table = "customers"
