from rest_framework import serializers

from nwevents.models import NWEvent
from nwlocationbound.models import NWCoordinate
from nwlocationbound.serializers import NWCoordinateSerializer

# TODO:
# Copy the logic from NWUsers here to allow the user
# to enter latitude and longitude and use a writeable
# serializer
class NWEventSerializer(serializers.ModelSerializer):

    location_coordinate = NWCoordinateSerializer()

    class Meta:
        model = NWEvent
        fields = '__all__'


        # Figure out why this doesnt work. Instead of finding, it will always try creating which causes problems
        # If worse comes to worst just manually do the logic
    def create(self, validated_data):

        coordinate_data = validated_data.pop("location_coordinate")

        coordinate = NWCoordinate.objects.get_or_create(
            latitude=coordinate_data.get("latitude"),
            longitude=coordinate_data.get("longitude"),
            defaults=coordinate_data
        )[0]

        new_event = NWEvent.objects.create(location_coordinate=coordinate, **validated_data)

        return new_event
