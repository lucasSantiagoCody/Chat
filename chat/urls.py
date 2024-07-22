from django.urls import path
from django.views.generic import TemplateView


urlpatterns = [
    path('chat/', TemplateView.as_view(template_name='chat.html'))
]