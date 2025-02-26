from rest_framework import serializers

from medspa.models.service import Service


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = ["id", "name", "description", "price", "duration", "medspa", "product"]
