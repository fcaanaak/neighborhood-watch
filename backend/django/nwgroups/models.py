from django.db import models

from nwlocationbound.models import NWLocationBound

class NWGroup(models.Model):
    name = models.CharField(max_length=64)
    password = models.CharField(max_length=64,blank=True)

    location_bound = models.ForeignKey(NWLocationBound, on_delete=models.PROTECT)
    # Implicit Fields

    # - user_membership (Defined in nwusers/models/nwuser.py)
    # - channels (Defined in nwchannels/models.py)

    def __str__(self):
        return self.name