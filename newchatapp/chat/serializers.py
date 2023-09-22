from rest_framework import serializers, exceptions
from django.contrib.auth.models import User

from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"