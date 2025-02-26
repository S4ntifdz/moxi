from django.contrib import admin
from medspa.models import ServiceProduct

@admin.register(ServiceProduct)
class ServiceProductAdmin(admin.ModelAdmin):
    list_display = ("name", "service_type", "supplier", "description",)
    list_filter = ("service_type", "supplier")
    search_fields = ("name",)
