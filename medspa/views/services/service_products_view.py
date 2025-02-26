from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination
from medspa.models.service_product import ServiceProduct
from medspa.serializers.services.service_product_serializer import (
    ServiceProductSerializer,
)


class ServiceProductPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = "page_size"
    max_page_size = 100


class ServiceProductViewSet(viewsets.ModelViewSet):
    queryset = ServiceProduct.objects.all().order_by("id")
    serializer_class = ServiceProductSerializer
    pagination_class = ServiceProductPagination
