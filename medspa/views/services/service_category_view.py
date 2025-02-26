from rest_framework import viewsets
from medspa.models.service_category import ServiceCategory
from medspa.serializers.services.service_category_serializer import (
    ServiceCategorySerializer,
)


class ServiceCategoryViewSet(viewsets.ModelViewSet):
    queryset = ServiceCategory.objects.all()
    serializer_class = ServiceCategorySerializer
