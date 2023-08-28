from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    USER_TYPE_CHOICES = [
        ('Client', 'Client'),
        ('Admin', 'Admin'),
    ]
    
    user_type = models.CharField(max_length=10, choices=USER_TYPE_CHOICES, default='Client')

    # Add related_name to avoid naming conflicts
    groups = None
    user_permissions = None

    def __str__(self):
        return self.username
