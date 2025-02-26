from rest_framework import viewsets

from medspa.models.medspa import Medspa
from medspa.serializers.medspas.medspa_serializer import MedspaSerializer


class MedspaViewSet(viewsets.ModelViewSet):
    queryset = Medspa.objects.all()
    serializer_class = MedspaSerializer
