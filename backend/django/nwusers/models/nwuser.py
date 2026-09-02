from django.db import models
from django.contrib.auth.models import User

from nwgroups.models import NWGroup

class NWUser(models.Model):
    auth_user = models.OneToOneField(User, on_delete=models.CASCADE)
    groups_joined = models.ManyToManyField(
        NWGroup,
        through= 'NWMembership',
        related_name='user_membership',
    )

    def __str__(self):
        return self.auth_user.username



