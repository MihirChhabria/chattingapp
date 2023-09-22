import json
from channels.generic.websocket import AsyncWebsocketConsumer
from .utils import set_user_status, get_online_users

class ChatRoomConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await set_user_status(self.scope['user'].id, True)
        online_users = await get_online_users()
        print('scope=',self.scope)
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.room_name

        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )


        await self.accept()
        await self.send(text_data=json.dumps({
            'type': 'online_users',
            'online_users': online_users
        }))

    async def disconnect(self, close_code):
        await set_user_status(self.scope['user'].id, False)
        print('scope_disconnect=',self.scope)
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        print('receive=',text_data)
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        username = text_data_json['username']

        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chatroom_message',
                'message': message,
                'username': username,
            }
        )

    async def chatroom_message(self, event):
        print('chatroom_message=',event)
        message = event['message']
        username = event['username']

        await self.send(text_data=json.dumps({
            'message': message,
            'username': username,
        }))

    pass