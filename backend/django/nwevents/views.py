from rest_framework import viewsets

from nwevents.models import NWEvent
from nwevents.serializers import NWEventSerializer


# Create your views here.
class NWEventViewSet(viewsets.ModelViewSet):
    queryset = NWEvent.objects.all()
    serializer_class = NWEventSerializer