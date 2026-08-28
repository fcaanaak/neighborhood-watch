# More to be added here later (see option 2: https://simpleisbetterthancomplex.com/tutorial/2016/07/22/how-to-extend-django-user-model.html)
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch.dispatcher import receiver

from nwgroups.models import NWGroup

class NWUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    groups_joined = models.ManyToManyField(NWGroup)

    def __str__(self):
        return self.user.username