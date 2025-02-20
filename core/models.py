from django.db import models
from django.contrib.auth.models import User


class Device(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    ip = models.GenericIPAddressField()
    is_active = models.BooleanField()


    def __repr__(self):
        return self.name
