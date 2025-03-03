from django.contrib import admin
from medspa.models.supplier import Supplier

@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    list_display = ("name", "description")
    search_fields = ("name",)
