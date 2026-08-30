from django.db import models

from nwgroups.models import NWGroup

# TODO:
# 0. See if a division query is actually needed to get all the users in a group or if a join will suffice
# 1. Rewrite the group division query to be a simple join if above applies
# 2. Create a method to get all channels in a group
# 3. Add that method to the groups viewset

class NWChannel(models.Model):
    name = models.CharField(max_length=64)
    description = models.TextField(max_length=256, blank=True)
    password = models.CharField(max_length=64, blank=True, null=True)
    datetime_created = models.DateTimeField(auto_now_add=True)

    owning_group = models.ForeignKey(NWGroup, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} | {self.description}"