from rest_framework import serializers
from .models import Region, Territories


class RegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = ['region_id', 'region_description']


class TerritoriesSerializer(serializers.ModelSerializer):
    region = RegionSerializer(read_only=True)
    region_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = Territories
        fields = [
            'territory_id',
            'territory_description',
            'region',
            'region_id',
        ]