from django import forms
from django.contrib import admin
from medspa.models.service import Service
@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ("name", "medspa", "get_products", "price", "duration")
    list_filter = ("medspa", "product")
    search_fields = ("name", "description")
    filter_horizontal = ("product",)

    def get_products(self, obj):
        return ", ".join([product.name for product in obj.get_products()])

    get_products.short_description = "Products"
