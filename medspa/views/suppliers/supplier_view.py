from rest_framework import viewsets

from medspa.models.supplier import Supplier
from medspa.serializers.suppliers.supplier_serializer import SupplierSerializer


class SupplierViewSet(viewsets.ModelViewSet):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer
