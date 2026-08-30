from django.db import models

from .nwuser import NWUser
from nwchannels.models import NWChannel

class NWSubscription(models.Model):
    class Role(models.TextChoices):
        ADMIN = 'ADMIN', "Admin"
        MEMBER = 'MEMBER', "Member"

    user = models.ForeignKey(NWUser, on_delete=models.CASCADE)
    channel = models.ForeignKey(NWChannel, on_delete=models.CASCADE)
    role = models.CharField(max_length=10, choices=Role.choices, default=Role.MEMBER)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['user', 'channel'], name='unique_user_subscription'
            )
        ]

    def __str__(self):
        return f'{self.user} - {self.channel} | {self.role}'