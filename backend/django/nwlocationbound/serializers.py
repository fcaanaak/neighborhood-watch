from rest_framework import serializers

from nwlocationbound.models import NWCoordinate


class NWCoordinateSerializer(serializers.ModelSerializer):
    class Meta:
        model = NWCoordinate
        fields = '__all__'