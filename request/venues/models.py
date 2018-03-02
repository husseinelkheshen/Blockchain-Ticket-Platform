from django.db import models

from globals.models import User

# Create your models here.
class Venue(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=1000)

    class Meta:
        unique_together = ("name", "location")

    def __str__(self):
        return self.name
