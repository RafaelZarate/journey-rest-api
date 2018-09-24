from rest_framework import serializers
from core.models import Journey


class JourneySerializer(serializers.ModelSerializer):
    class Meta:
        model = Journey
        fields = '__all__'

