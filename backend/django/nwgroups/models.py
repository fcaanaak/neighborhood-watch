from django.db import models

# Create your models here.
class NWGroup(models.Model):
    name = models.CharField(max_length=64)
    password = models.CharField(max_length=64,blank=True)

    def __str__(self):
        return self.name