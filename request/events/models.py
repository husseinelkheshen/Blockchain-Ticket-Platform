from django.db import models
from datetime import datetime

from venues.models import Venue

# Create your models here.
class Event(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    venue = models.ForeignKey(Venue, on_delete=models.CASCADE)
    when = models.DateTimeField(default = datetime.now())

    def __str__(self):
        return self.name
