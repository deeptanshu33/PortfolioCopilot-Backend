import json
from channels.generic.websocket import AsyncWebsocketConsumer  # type: ignore[import]

class TestConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.ws_id = self.scope["url_route"]["kwargs"]["ws_id"]
        self.group_name = f"agent_{self.ws_id}"
        
        await self.channel_layer.group_add(
            self.group_name,
            self.channel_name
        )

        print(f"connected to group: {self.group_name}")

        await self.accept()
    
    async def disconnect(self, code):
        await self.channel_layer.group_discard(
            self.group_name,
            self.channel_name
        )

    async def send_update(self, event):
        print(f"Recieved from group: {event}")

        await self.send(text_data=json.dumps(event['data']))