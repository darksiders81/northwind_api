from rest_framework import serializers
from .models import Products


class ProductsSerializer(serializers.ModelSerializer):
    # نمایش نام category و supplier به جای فقط ID
    category_name = serializers.CharField(
        source="category.category_name", read_only=True
    )
    supplier_name = serializers.CharField(
        source="supplier.company_name", read_only=True
    )

    class Meta:
        model = Products
        fields = [
            "product_id",
            "product_name",
            "supplier",
            "supplier_name",
            "category",
            "category_name",
            "quantity_per_unit",
            "unit_price",
            "units_in_stock",
            "units_on_order",
            "reorder_level",
            "discontinued",
        ]
