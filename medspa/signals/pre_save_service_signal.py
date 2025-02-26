from django.db.models.signals import m2m_changed, pre_save
from django.dispatch import receiver
from medspa.models.appointment import Appointment

def calculate_totals(instance):
    instance.total_duration = instance.get_total_duration()
    instance.total_price = instance.get_total_price()

@receiver(m2m_changed, sender=Appointment.services.through)
def update_totals(sender, instance, **kwargs):
    if instance.pk:
        calculate_totals(instance)
        instance.save(update_fields=['total_duration', 'total_price', 'end_time'])

@receiver(pre_save, sender=Appointment)
def set_totals(sender, instance, **kwargs):
    if instance.pk:
        calculate_totals(instance)