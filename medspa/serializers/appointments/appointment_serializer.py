from rest_framework import serializers
from medspa.models.appointment import Appointment

class AppointmentSerializer(serializers.ModelSerializer):
    total_duration = serializers.IntegerField(read_only=True)
    total_price = serializers.DecimalField(
        max_digits=10, decimal_places=2, read_only=True
    )

    class Meta:
        model = Appointment
        fields = [
            "id",
            "medspa",
            "start_time",
            "services",
            "status",
            "total_duration",
            "total_price",
        ]

    def validate(self, data):
        if self.instance and 'status' in data and 'services' not in data:
            return data
        if 'services' not in data:
            raise serializers.ValidationError(
                "Services must be specified for the appointment"
            )
        return data