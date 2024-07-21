from .consumers import ChatConsumer
from django.urls import re_path

websocket_urlpatterns = [
    re_path('ws/chat/(?P<roo_name>\w+)/$', ChatConsumer.as_agi())
]