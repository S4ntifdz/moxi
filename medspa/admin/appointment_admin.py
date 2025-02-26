from django.contrib import admin
from medspa.models.appointment import Appointment

@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = (
        "medspa",
        "start_time",
        "end_time",
        "status",
        "get_total_duration",
        "get_total_price",
    )
    
    list_filter = ("status", "medspa")
    search_fields = ("medspa__name",)
    filter_horizontal = ("services",)
    exclude = (
            'total_duration',
            'total_price',
            'end_time',
        )
    def get_total_duration(self, obj):
        return f"{obj.total_duration} minutes"

    get_total_duration.short_description = "Duration"

    def get_total_price(self, obj):
        return f"${obj.total_price}"

    get_total_price.short_description = "Price"
