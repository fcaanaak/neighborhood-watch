from rest_framework import serializers

from nwevents.models import NWEvent


class NWEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = NWEvent
        fields = '__all__'

