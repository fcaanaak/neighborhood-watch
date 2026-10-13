from rest_framework import serializers

from nwlocationbound.models import NWCoordinate, NWLocationBound

class NWCoordinateSerializer(serializers.ModelSerializer):
    class Meta:
        model = NWCoordinate
        fields = '__all__'
        validators = []

class NWLocationBoundSerializer(serializers.ModelSerializer):

    coordinates = NWCoordinateSerializer(many=True,allow_empty=False)

    class Meta:
        model = NWLocationBound
        fields = '__all__'

    def create(self, validated_data):
        coordinate_data = validated_data.pop("coordinates")

        new_coordinates = []

        for coordinate in coordinate_data:
            retrieved, created = NWCoordinate.objects.get_or_create(
                latitude=coordinate.get("latitude"),
                longitude=coordinate.get("longitude")
            )

            new_coordinates.append(retrieved)

        new_locationbound = NWLocationBound.objects.create()
        new_locationbound.coordinates.set(new_coordinates)

        return new_locationbound