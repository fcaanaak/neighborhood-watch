from django.db import models

class NWGroup(models.Model):
    name = models.CharField(max_length=64)
    password = models.CharField(max_length=64,blank=True)

    # There is an implicit field for the users in a group called
    # user_membership. This is defined in nwusers/models/nwuser.py

    # Implicit Fields

    # user_membership (Defined in nwusers/models/nwuser.py)
    # channels (Defined in nwchannels/models.py)

    def __str__(self):
        return self.name