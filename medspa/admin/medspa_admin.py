from django.contrib import admin
from medspa.models import Medspa


@admin.register(Medspa)
class MedspaAdmin(admin.ModelAdmin):
    list_display = ("name", "phone_number", "email")
    search_fields = ("name", "email", "phone_number")
