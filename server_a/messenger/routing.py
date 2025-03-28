from django.urls import re_path
from .consumers import MessengerConsumer

websocket_urlpatterns = [
    re_path(r'ws/messenger/$', MessengerConsumer.as_asgi()),
]