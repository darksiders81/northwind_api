from rest_framework import serializers
from .models import UsStates


class UsStatesSerializer(serializers.ModelSerializer):
    class Meta:
        model = UsStates
        fields = [
            'state_id',
            'state_name',
            'state_abbr',
            'state_region',
        ]