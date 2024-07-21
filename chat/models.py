from django.db import models


class Room(models.Model):
    room = models.CharField(max_length=50)

class Message(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)