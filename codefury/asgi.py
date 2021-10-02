"""
ASGI config for codefury project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/asgi/
"""
import os

import django
from channels.http import AsgiHandler
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
import quiz.routing

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'codefury.settings')
django.setup()

application = ProtocolTypeRouter({
  "http": AsgiHandler(),
  "websocket": AuthMiddlewareStack(
        URLRouter(
            quiz.routing.websocket_urlpatterns
        )
    ),
  # Just HTTP for now. (We can add other protocols later.)
})