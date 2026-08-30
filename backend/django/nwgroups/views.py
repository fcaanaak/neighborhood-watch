from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from django.core import serializers

from nwusers.models import NWUser
from nwgroups.models import NWGroup
from nwgroups.serializers import NWGroupSerializer

# Create your views here.
class NWGroupViewSet(viewsets.ModelViewSet):
    queryset = NWGroup.objects.all()
    serializer_class = NWGroupSerializer

    @action(methods=['get'], detail=True)
    def get_members(self, request, pk=None):

        if not self.queryset.filter(id=pk).exists():
            return Response("No such group exists", status=status.HTTP_404_NOT_FOUND)

        usernames = NWUser.objects.raw(""" 
                            select username, id from auth_user
                            where id in (
                                select user_id from nwusers_nwmembership m
                                where not exists(
                                        (select id from nwgroups_nwgroup where id=%s)
                                        except
                                        (select mm.group_id from nwusers_nwmembership mm where mm.group_id = m.group_id)
                                )
                            );
        """, params=[pk])

        return Response({'members': [user.username for user in usernames]})


