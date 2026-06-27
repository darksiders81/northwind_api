from rest_framework import serializers
from .models import Customers, CustomerDemographics, CustomerCustomerDemo


class CustomerDemographicsSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerDemographics
        fields = ["customer_type_id", "customer_desc"]


class CustomersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customers
        fields = [
            "customer_id",
            "company_name",
            "contact_name",
            "contact_title",
            "address",
            "city",
            "region",
            "postal_code",
            "country",
            "phone",
            "fax",
        ]


class CustomerCustomerDemoSerializer(serializers.ModelSerializer):
    # نمایش اطلاعات کامل به جای فقط ID
    customer = CustomersSerializer(read_only=True)
    customer_type = CustomerDemographicsSerializer(read_only=True)

    # برای write از ID استفاده میکنیم
    customer_id = serializers.CharField(write_only=True)
    customer_type_id = serializers.CharField(write_only=True)

    class Meta:
        model = CustomerCustomerDemo
        fields = [
            "customer",
            "customer_type",
            "customer_id",
            "customer_type_id",
        ]
