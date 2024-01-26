from django.urls import path
from . import consumers

websocket_urlpatterns = [
    path('ws_connect/', consumers.RouteHandlerConsumer.as_asgi()),
]
