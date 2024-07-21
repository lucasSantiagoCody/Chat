from django.db import models


class Room(models.Model):
    room = models.CharField(max_length=50)
    