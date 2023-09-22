from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    is_online = models.BooleanField(default=False)

    def __str__(self):
        return self.username

class Room(models.Model):
    name=models.CharField(max_length=20)
    slug=models.SlugField(max_length=10)

    def __str__(self):
        return self.name
    
class Message(models.Model):
    content=models.TextField()    
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    room=models.ForeignKey(Room,on_delete=models.CASCADE)
    created_on=models.DateTimeField(auto_now_add=True)
