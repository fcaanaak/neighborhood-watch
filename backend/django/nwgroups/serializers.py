from rest_framework import serializers

from nwgroups.models import NWGroup
from nwlocationbound.models import NWLocationBound, NWCoordinate
from nwlocationbound.serializers import NWLocationBoundSerializer

class NWGroupSerializer(serializers.ModelSerializer):

    location_bound = NWLocationBoundSerializer(allow_null=False)

    class Meta:
        model = NWGroup
        fields = "__all__"
        extra_kwargs = {"password": {"write_only":True}}

    def create(self, validated_data):
        location_bound_data = validated_data.pop("location_bound")

        new_location_bound = NWLocationBound.objects.create()

        new_location_bound.coordinates.set([
            NWCoordinate.objects.get_or_create(
                latitude=coord.get("latitude"),
                longitude=coord.get("longitude")
            )[0].pk for coord in location_bound_data.get("coordinates")
        ])

        return NWGroup.objects.create(location_bound=new_location_bound,**validated_data)