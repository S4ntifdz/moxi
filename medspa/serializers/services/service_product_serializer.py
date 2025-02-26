from rest_framework import serializers

from medspa.models.service_product import ServiceProduct


class ServiceProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceProduct
        fields = "__all__"
