from asgiref.sync import sync_to_async
from .models import User
from .serializers import UserSerializer
from django.http import JsonResponse

@sync_to_async
def set_user_status(uid, state):
    User.objects.filter(id=uid).update(is_online=state)

@sync_to_async
def get_online_users():
    # online_users = User.objects.filter(is_online=True).count()
    online_users = User.objects.filter(is_online=True)
    user_serializer = UserSerializer(online_users, many=True)
    return user_serializer.data
