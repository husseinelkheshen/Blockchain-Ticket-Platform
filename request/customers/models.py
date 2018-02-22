from decimal import Decimal

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Customer(models.Model):
    """
    Users that buy tickets.
    """

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # store up to but not including ten trillion dollars
    balance = models.DecimalField(
            max_digits=15, decimal_places=2, default=Decimal("0.00"))

    def __str__(self):
        return self.user.username
