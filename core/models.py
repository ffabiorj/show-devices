from django.db import models


class Device(models.Model):
    name = models.CharField(max_length=50)
    ip = models.GenericIPAddressField()
    is_active = models.BooleanField()


    def __repr__(self):
        return self.name
