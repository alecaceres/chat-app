import json
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async
from ChatApp.models import Message, Room

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        room_name = self.scope['url_route']['kwargs']['room_name']
        # Sanitize room name to remove any invalid characters
        sanitized_room_name = "".join(c for c in room_name if c.isalnum() or c in "-_")
        self.room_name = f"room_{sanitized_room_name}"
        await self.channel_layer.group_add(self.room_name, self.channel_name)
        await self.accept()


    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(self.room_name, self.channel_name)

    async def receive(self, text_data):
        message = json.loads(text_data)
        event = {
            "type": "send_message",
            "message": message,
        }

        await self.channel_layer.group_send(self.room_name, event)

    async def send_message(self, event):
        data = event["message"]
        await self.create_message(data=data)
        response_data = {
            "sender": data["sender"],
            "message": data["message"],
        }
        await self.send(text_data=json.dumps({"message": response_data}))

    @database_sync_to_async
    def create_message(self, data):
        room = Room.objects.get(room_name=data["room_name"])
        Message.objects.get_or_create(
            room=room,
            sender=data["sender"],
            message=data["message"]
        )