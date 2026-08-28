from rest_framework import viewsets
from nwgroups.models import NWGroup
from nwgroups.serializers import NWGroupSerializer

# Create your views here.
class NWGroupViewSet(viewsets.ModelViewSet):
    queryset = NWGroup.objects.all()
    serializer_class = NWGroupSerializer
