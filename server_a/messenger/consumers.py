import json
from channels.generic.websocket import AsyncWebsocketConsumer

class MessengerConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.group_name = 'messenger_group'
        await self.channel_layer.group_add(self.group_name, self.channel_name)
        await self.accept()
        print(f"WebSocket connected: {self.channel_name}")

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(self.group_name, self.channel_name)
        print(f"WebbSocket disconnected: {self.channel_name}")

    async def send_message(self, event):
        message = event['message']
        await self.send(text_data=json.dumps({
            'message': message
        }))