from django.shortcuts import render
from rest_framework import viewsets

from nwlocationbound.models import NWLocationBound
from nwlocationbound.serializers import NWLocationBoundSerializer


# Create your views here.

class NWLocationBoundViewSet(viewsets.ModelViewSet):
    queryset = NWLocationBound.objects.all()
    serializer_class = NWLocationBoundSerializer