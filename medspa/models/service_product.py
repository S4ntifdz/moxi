from django.db import models

from medspa.models.service_type import ServiceType
from medspa.models.supplier import Supplier


class ServiceProduct(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    service_type = models.ForeignKey(
        ServiceType, on_delete=models.CASCADE, related_name="products"
    )
    supplier = models.ForeignKey(
        Supplier,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="products",
    )

    def __str__(self):
        return self.name
