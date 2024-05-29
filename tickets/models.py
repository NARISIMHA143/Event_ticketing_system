

# Create your models here.
from django.db import models

# Create your models here.
from django.contrib.auth.models import User

class Profile(models.Model):
    USER_TYPES = (
        ('event_manager', 'Event Manager'),
        ('book', 'Book'),
        ('editor', 'Editor'),
        ('admin', 'Admin'),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_type = models.CharField(max_length=20, choices=USER_TYPES)

    def _str_(self):
        return f"{self.user.username}'s Profile"