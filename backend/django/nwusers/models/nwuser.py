from django.db import models
from django.contrib.auth.models import User

from nwgroups.models import NWGroup

class NWUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    groups_joined = models.ManyToManyField(
        NWGroup,
        through= 'NWMembership',
        related_name='nwgroups',
    )

    def __str__(self):
        return self.user.username



