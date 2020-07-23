from rest_framework import serializers
from .models import Player
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
# player serializer


class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = "__all__"
