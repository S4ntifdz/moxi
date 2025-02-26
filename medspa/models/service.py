from django.db import models

from medspa.models.medspa import Medspa
from medspa.models.service_product import ServiceProduct


class Service(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    duration = models.IntegerField(help_text="Duration in minutes")
    medspa = models.ForeignKey(
        Medspa, on_delete=models.CASCADE, related_name="services"
    )
    product = models.ManyToManyField(ServiceProduct, related_name='services')


    def __str__(self):
        return f"{self.name} at {self.medspa.name}"

    def get_products(self):
        return self.product.all()
    
    def get_category(self):
        categories = self.product.values_list('service_type__category__name', flat=True).distinct()
        return ", ".join(categories)
