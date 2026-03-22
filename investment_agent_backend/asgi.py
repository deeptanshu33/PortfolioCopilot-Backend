"""
ASGI config for investment_agent_backend project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/6.0/howto/deployment/asgi/
"""

import os
from channels.routing import ProtocolTypeRouter, URLRouter #type: ignore
from django.urls import path
from research.consumer import TestConsumer
from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'investment_agent_backend.settings')

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": URLRouter([
        path("ws/agent/<str:ws_id>/", TestConsumer.as_asgi(), name='test-ws'),
    ]),
})


