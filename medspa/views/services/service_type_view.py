from rest_framework import viewsets
from medspa.models.service_type import ServiceType
from medspa.serializers.services.service_type_serializer import ServiceTypeSerializer


class ServiceTypeViewSet(viewsets.ModelViewSet):
    queryset = ServiceType.objects.all()
    serializer_class = ServiceTypeSerializer
