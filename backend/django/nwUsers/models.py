from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=16, primary_key=True)
    password = models.CharField(max_length=64)
    datetime_joined = models.DateTimeField(auto_now_add=True,editable=False)

    def __str__(self):
        return self.username