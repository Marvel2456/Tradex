from django.db import models
from django.contrib.auth.models import User
import uuid
import random
# Create your models here.

class Trader(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
    balance = models.DecimalField(max_digits=10, default=100, decimal_places=2, blank=True, null=True)


    def __str__(self):
        return self.user.username
    

class Trade(models.Model):
    trader = models.ForeignKey(Trader, on_delete=models.CASCADE, blank=True, null=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    profit_loss = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    def __str__(self):
        return f"{self.trader.user.username} - {self.timestamp}"