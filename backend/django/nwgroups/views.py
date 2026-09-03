from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from django.core import serializers

from nwusers.models import NWUser
from nwgroups.models import NWGroup
from nwgroups.serializers import NWGroupSerializer

def group_exists(pk):
    try:
        NWGroup.objects.get(id=pk)
        return True
    except NWGroup.DoesNotExist:
        return False


class NWGroupViewSet(viewsets.ModelViewSet):
    queryset = NWGroup.objects.all()
    serializer_class = NWGroupSerializer


    @action(methods=['get'], detail=True, url_path='members')
    def get_members(self, request, pk=None):

        if not group_exists(pk):
            return Response("No such group exists", status=status.HTTP_404_NOT_FOUND)

        query_group = NWGroup.objects.filter(id=pk).prefetch_related('user_membership').first()
        usernames = [user.auth_user.username for user in query_group.user_membership.all()]

        return Response({'members': usernames})

    @action(methods=['get'], detail=True, url_path='channels')
    def get_channels(self, request, pk=None):
        if not group_exists(pk):
            return Response("No such group exists", status=status.HTTP_404_NOT_FOUND)

        query_group = NWGroup.objects.filter(id=pk).prefetch_related('channels').first()
        channel_names = [channel.name for channel in query_group.channels.all()]

        return Response({'channel_names': channel_names})

    @action(methods=['get'], detail=True, url_path='location_bound')
    def get_location_bound(self, request, pk=None):

        if not group_exists(pk):
            return Response("No such group exists", status=status.HTTP_404_NOT_FOUND)

        query_group = NWGroup.objects.filter(id=pk).prefetch_related('location_bound__coordinates').first()

        coordinates = [[coord.latitude, coord.longitude] for coord in query_group.location_bound.coordinates.all()]

        return Response({'location_bound': coordinates})


