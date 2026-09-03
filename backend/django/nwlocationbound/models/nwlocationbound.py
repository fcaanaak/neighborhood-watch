from django.db import models

from nwlocationbound.models import NWCoordinate

class NWLocationBound(models.Model):
    """
    Location boundary which will be managed by a group

    Currently, its just a container for coordinates.
    However, later (if implemented) it will store aggregate metadata
    based on its constituent coordinates.
    """
    coordinates = models.ManyToManyField(
        NWCoordinate,
        related_name='location_coordinates',
    )
