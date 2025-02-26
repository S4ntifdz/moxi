from django.contrib import admin

from medspa.models.service_category import ServiceCategory


@admin.register(ServiceCategory)
class ServiceCategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "description")
    search_fields = ("name",)
