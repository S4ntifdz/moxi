from rest_framework import viewsets, filters

from medspa.models.service import Service
from medspa.serializers.services.service_serializer import ServiceSerializer


class ServiceViewSet(viewsets.ModelViewSet):
    serializer_class = ServiceSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ["name", "description"]

    def get_queryset(self):
        queryset = Service.objects.all()
        medspa_id = self.request.query_params.get("medspa", None)
        if medspa_id is not None:
            queryset = queryset.filter(medspa_id=medspa_id)
        return queryset
