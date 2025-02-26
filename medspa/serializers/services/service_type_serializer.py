from rest_framework import serializers

from medspa.models.service_type import ServiceType


class ServiceTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceType
        fields = "__all__"
