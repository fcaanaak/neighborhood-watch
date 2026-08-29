from django.db import models, transaction
from django.db.models.signals import pre_delete
from django.dispatch import receiver
from rest_framework.exceptions import ValidationError

from .nwuser import NWUser
from nwgroups.models import NWGroup

class NWMembership(models.Model):
    class Role(models.TextChoices):
        ADMIN = 'ADMIN', "Admin"
        MEMBER = 'MEMBER', "Member"

    user = models.ForeignKey(NWUser, on_delete=models.CASCADE)
    group = models.ForeignKey(NWGroup, on_delete=models.CASCADE)
    role = models.CharField(max_length=10, choices=Role.choices, default=Role.MEMBER)
    joined_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['user', 'group'], name='unique_user_membership'
            )
        ]

    def __str__(self):
        return f'{self.user} - {self.group} | {self.role}'

def get_num_admins_in_group(group, pk_to_exclude=None):
    """
    Get the number of admins inside of a group

    :param group: The NWGroup object we want to find the number of admins inside
    :param pk_to_exclude: The primary key of the admin-group relationship row we wish to exclude (if any)

    :return: The number of admins inside the group provided not including those which participate in relationships with
    pk_to_exclude
    """
    admins = NWMembership.objects.filter(group=group, role=NWMembership.Role.ADMIN)

    if pk_to_exclude:
        admins = admins.exclude(pk=pk_to_exclude)

    return admins.count()

# Enforce total participation on the groups side
@receiver(pre_delete, sender=NWMembership)
def prevent_last_admin_deletion(sender, instance, **kwargs):
    if instance.role == NWMembership.Role.ADMIN:
        with transaction.atomic():
            other_admins_count = get_num_admins_in_group(instance.group, instance.pk)
            if other_admins_count == 0:
                raise ValidationError(
                    "Cannot remove the last admin of a group"
                )