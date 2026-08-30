from rest_framework import serializers

from nwgroups.models import NWGroup


class NWGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = NWGroup
        fields = "__all__"
        extra_kwargs = {"password": {"write_only":True}}
