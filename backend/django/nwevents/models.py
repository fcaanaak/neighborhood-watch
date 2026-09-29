from django.db import models

from nwchannels.models import NWChannel
from nwlocationbound.models import NWCoordinate
from nwusers.models import NWUser

class NWEvent(models.Model):

    name = models.CharField(max_length=64)
    description = models.TextField(blank=True)
    time_created = models.DateTimeField(auto_now_add=True)

    location_coordinate = models.ForeignKey(NWCoordinate, on_delete=models.SET_NULL, null=True)
    contained_channel = models.ForeignKey(NWChannel, on_delete=models.CASCADE)
    creator = models.ForeignKey(NWUser, on_delete=models.SET_NULL, null=True)

    def __str__(self) -> str:
        return f"{self.name} @ {self.location_coordinate}"