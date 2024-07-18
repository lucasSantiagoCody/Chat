from .forms import CustomUserChangeForm, CustomUserCreationForm
from django.contrib.admin import ModelAdmin
from django.contrib import admin
from .models import User


class UserAdmin(ModelAdmin):
    model = User
    form = CustomUserChangeForm
    add_form = CustomUserCreationForm
    list_display = ['username', 'is_staff', 'is_superuser']
    list_filter = ['email', 'is_superuser']

admin.site.register(User, UserAdmin)