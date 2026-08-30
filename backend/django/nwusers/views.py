from django.contrib.auth.models import User
from rest_framework import viewsets

from .models import NWUser
from .serializers import NWUserSerializer, UserSerializer


# Create your views here.
class NWUserViewSet(viewsets.ModelViewSet):
    queryset = NWUser.objects.all()
    serializer_class = NWUserSerializer
