from rest_framework import serializers
from .models import Categories


class CategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categories
        fields = ["category_id", "category_name", "description"]

