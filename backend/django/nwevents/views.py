from typing import Any

from rest_framework import viewsets
from rest_framework.request import Request
from rest_framework.response import Response

from nwevents.models import NWEvent
from nwevents.serializers import NWEventSerializer


class NWEventViewSet(viewsets.ModelViewSet):
    queryset = NWEvent.objects.all()
    serializer_class = NWEventSerializer

    def create(self, request: Request, *args: Any, **kwargs: Any) -> Response:
        return super().create(request, *args, **kwargs)
