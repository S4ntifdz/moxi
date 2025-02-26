from django.contrib import admin
from medspa.models.service_type import ServiceType


@admin.register(ServiceType)
class ServiceTypeAdmin(admin.ModelAdmin):
    list_display = ("name", "category", "description")
    list_filter = ("category",)
    search_fields = ("name",)
