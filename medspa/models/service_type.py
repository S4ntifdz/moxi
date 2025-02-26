from django.db import models

from medspa.models.service_category import ServiceCategory


class ServiceType(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    category = models.ForeignKey(
        ServiceCategory, on_delete=models.CASCADE, related_name="types"
    )

    def __str__(self):
        return self.name
