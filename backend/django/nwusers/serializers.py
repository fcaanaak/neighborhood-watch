from django.contrib.auth.models import User
from rest_framework import serializers

from .models import NWUser

# Reference used here: https://unwiredlearning.com/blog/drf-writable-nested

class UserSerializer(serializers.ModelSerializer):
    """
    Serializer for the builtin User models that NWUser extends.
    """
    class Meta:
        model = User
        fields = ("username","password","email")
        extra_kwargs = {"password": {"write_only": True}}

class NWUserSerializer(serializers.ModelSerializer):
    """
    Serializer for NWUser model.
    """
    user = UserSerializer()

    class Meta:
        model = NWUser
        fields = ["user"]

    def create(self, validated_data):
        user_data = validated_data.pop("user")

        new_user = User.objects.create_user(**user_data)

        nw_user = NWUser.objects.create(user=new_user,**validated_data)

        return nw_user