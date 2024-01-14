from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class CustomUser(AbstractUser):
    name = models.CharField(max_length=128, blank=True)
    
    def __str__(self) -> str:
        return self.email


class FollowingSystem(models.Model):
    follower = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="follower")
    follows = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="follows")