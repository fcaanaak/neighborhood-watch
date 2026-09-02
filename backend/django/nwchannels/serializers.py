from rest_framework import serializers

from .models import NWChannel


class NWChannelSerializer(serializers.ModelSerializer):
    class Meta:
        model = NWChannel
        fields = '__all__'
        extra_kwargs = {"password":{"write_only":True}}