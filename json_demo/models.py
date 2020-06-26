from django.db import models
import datetime
from django.utils import timezone


# Create your models here.

class UserDetails(models.Model):

    #Id = models.CharField(max_length=100)
    real_name = models.CharField(max_length=255)
    tz = models.CharField(max_length=20, default='default_city')
    start_time = models.DateTimeField(default=timezone.now)
    end_time = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.real_name
