from django.db import models

from nwgroups.models import NWGroup

class NWChannel(models.Model):
    name = models.CharField(max_length=64)
    description = models.TextField(max_length=256, blank=True)
    password = models.CharField(max_length=64, blank=True, null=True)
    datetime_created = models.DateTimeField(auto_now_add=True)
    owning_group = models.ForeignKey(NWGroup, on_delete=models.CASCADE, related_name='channels')

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['name', 'owning_group'],
                name='nw_channel_',
            )
        ]

    def __str__(self):
        return f"{self.name} | {self.description}"