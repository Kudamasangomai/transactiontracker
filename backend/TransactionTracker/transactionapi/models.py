from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class Transactions(models.Model):
    amount = models.CharField(max_length = 10)
    description = models.CharField(max_length = 180)
    created_at = models.DateTimeField(auto_now_add = True, auto_now = False, blank = True)
    updated_at = models.DateTimeField(auto_now = True, blank = True)
    user = models.ForeignKey(User, on_delete = models.CASCADE, blank = True, null = True)

    class Meta:
        ordering = ['created_at']
    
    def __str__(self):
        return f"{self.created_at} - ${self.amount} - {self.description}"
