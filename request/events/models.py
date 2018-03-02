from django.db import models

from venues.models import Venue

# Create your models here.
class Event(models.Model):
    name = models.CharField(max_length=100)
    venue = models.ForeignKey(Venue)

    def __str__(self):
        return self.name
