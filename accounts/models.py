
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    # add additional fields in here
    address  = models.TextField()
    number   = models.PositiveIntegerField(null=True,blank=True)
    is_admin = models.BooleanField(default=False)
    
    def __str__(self):
        return self.username