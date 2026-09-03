from django.db import models

class NWCoordinate(models.Model):
    """
    Location coodinate contained within a
    location boundary. Latitude and longitude are both
    five decimal places as per GPS standard.
    """
    coordinate_precision = 5
    latitude_digits = 2 + coordinate_precision
    longitude_digits = 3 + coordinate_precision

    latitude = models.DecimalField(max_digits=latitude_digits, decimal_places= coordinate_precision)
    longitude = models.DecimalField(max_digits=longitude_digits, decimal_places=coordinate_precision)

    def __str__(self):
        return f"({self.latitude}, {self.longitude})"

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['latitude', 'longitude'],
                name='unique_latitude_longitude'
            )
        ]