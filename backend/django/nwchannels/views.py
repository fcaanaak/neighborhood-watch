from django.shortcuts import render
from rest_framework import viewsets

from .models import NWChannel
from .serializers import NWChannelSerializer


# Create your views here.
class NWChannelViewSet(viewsets.ModelViewSet):
    queryset = NWChannel.objects.all()
    serializer_class = NWChannelSerializer