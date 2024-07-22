from django.contrib import admin
from django.urls import path, include
from .api import api

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', api.urls),
    path('chat/', include('chat.urls')),

]
