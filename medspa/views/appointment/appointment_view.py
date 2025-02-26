from datetime import datetime
from rest_framework import viewsets

from medspa.models.appointment import Appointment
from medspa.serializers.appointments.appointment_serializer import AppointmentSerializer


class AppointmentViewSet(viewsets.ModelViewSet):
    serializer_class = AppointmentSerializer

    def get_queryset(self):
        queryset = Appointment.objects.all()

        # Filter by status if provided
        status = self.request.query_params.get("status", None)
        if status:
            queryset = queryset.filter(status=status)

        # Filter by date if provided
        date = self.request.query_params.get("date", None)
        if date:
            try:
                date_obj = datetime.strptime(date, "%Y-%m-%d").date()
                queryset = queryset.filter(start_time__date=date_obj)
            except ValueError:
                pass

        return queryset
