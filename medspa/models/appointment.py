from django.db import models
from datetime import timedelta
from medspa.models.medspa import Medspa
from medspa.models.service import Service

class Appointment(models.Model):
    STATUS_CHOICES = [
        ("scheduled", "Scheduled"),
        ("completed", "Completed"),
        ("canceled", "Canceled"),
    ]

    medspa = models.ForeignKey(
        Medspa, on_delete=models.CASCADE, related_name="appointments"
    )
    start_time = models.DateTimeField()
    end_time = models.DateTimeField(blank=True, null=True)
    total_duration = models.IntegerField(blank=True, null=True)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    services = models.ManyToManyField(Service, related_name="appointments")
    status = models.CharField(
        max_length=10, choices=STATUS_CHOICES, default="scheduled"
    )

    def get_total_duration(self):
        return sum(service.duration for service in self.services.all())

    def get_total_price(self):
        return sum(service.price for service in self.services.all())

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.total_duration = self.get_total_duration()
        self.total_price = self.get_total_price()
        self.end_time = self.start_time + timedelta(minutes=self.total_duration)
        super().save(update_fields=['total_duration', 'total_price', 'end_time'])
    
    def __str__(self):
        return f"Appointment at {self.medspa.name} on {self.start_time}"