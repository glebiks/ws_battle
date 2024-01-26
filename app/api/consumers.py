from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async
from rest_framework_simplejwt.tokens import AccessToken
from django.contrib.auth.models import User
import json


class RouteHandlerConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        token = self.scope["query_string"].decode().split('=')[1]
        user = await self.get_user(token)
        if user:
            await self.accept()
        else:
            await self.close()

    async def disconnect(self, close_code):
        # Действия при отключении пользователя
        pass

    async def receive(self, text_data):
        # Обработка входящего текстового сообщения
        data = json.loads(text_data)
        action = data.get('action')

        if action == 'action1':
            await self.action1_handler(data)
        elif action == 'action2':
            await self.action2_handler(data)
        else:
            await self.send(text_data=json.dumps({
                'error': 'Invalid action',
            }))

    async def action1_handler(self, data):
        # Обработка действия 1
        pass

    async def action2_handler(self, data):
        # Обработка действия 2
        pass

    @database_sync_to_async
    def get_user(self, token):
        try:
            access_token = AccessToken(token)
            return User.objects.get(id=access_token['user_id'])
        except Exception as e:
            return None
