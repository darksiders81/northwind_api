from rest_framework import serializers
from .models import Shippers


class ShippersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shippers
        fields = ['shipper_id', 'company_name', 'phone']