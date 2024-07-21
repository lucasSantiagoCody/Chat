from .utils import generate_random_string
from django.db import models
from user.models import User


class Room(models.Model):
    token = models.CharField(max_length=255, unique=True, blank=True)
    room = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.token:
            self.token = generate_random_string(30)

        return super(Room, self).save(*args, **kwargs)

    def __str__(self):
        return self.room

class Message(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    sender = models.ForeignKey(
        User, 
        on_delete=models.CASCADE,
        related_name='user_sender'
        )
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)