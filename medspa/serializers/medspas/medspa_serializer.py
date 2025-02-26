from rest_framework import serializers

from medspa.models.medspa import Medspa


class MedspaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medspa
        fields = ["id", "name", "address", "phone_number", "email"]
