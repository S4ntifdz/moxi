from rest_framework import serializers

from medspa.models.service_category import ServiceCategory


class ServiceCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceCategory
        fields = "__all__"
