from rest_framework import serializers
from .models import Orders, OrderDetails


class OrderDetailsSerializer(serializers.ModelSerializer):
    product_name = serializers.CharField(source="product.product_name", read_only=True)

    class Meta:
        model = OrderDetails
        fields = [
            "order",
            "product",
            "product_name",
            "unit_price",
            "quantity",
            "discount",
        ]


class OrdersSerializer(serializers.ModelSerializer):
    # نمایش اطلاعات مرتبط
    customer_name = serializers.CharField(
        source="customer.company_name", read_only=True
    )
    employee_name = serializers.SerializerMethodField(read_only=True)
    shipper_name = serializers.CharField(source="ship_via.company_name", read_only=True)

    # نمایش order details داخل order
    order_details = OrderDetailsSerializer(
        many=True, read_only=True, source="orderdetails_set"
    )

    class Meta:
        model = Orders
        fields = [
            "order_id",
            "customer",
            "customer_name",
            "employee",
            "employee_name",
            "order_date",
            "required_date",
            "shipped_date",
            "ship_via",
            "shipper_name",
            "freight",
            "ship_name",
            "ship_address",
            "ship_city",
            "ship_region",
            "ship_postal_code",
            "ship_country",
            "order_details",
        ]

    def get_employee_name(self, obj):
        if obj.employee:
            return f"{obj.employee.first_name} {obj.employee.last_name}"
        return None
