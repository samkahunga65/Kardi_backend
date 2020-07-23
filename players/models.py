from django.db import models
from django.contrib.auth.models import User


class Player(models.Model):
    name = models.CharField(max_length=120)
    username = models.CharField(max_length=30, unique=True)
    chips = models.IntegerField(default=250)
    gold = models.IntegerField(default=0)
    friends = models.ManyToManyField(
        User, related_name="friends", blank=True)
    img = models.FileField(upload_to='media/', blank=True, null=True)
    owner = models.ForeignKey(
        User, related_name="player", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username
