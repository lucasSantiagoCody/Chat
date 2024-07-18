from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager):
    def create_user(self, username, email, password=None, **extra_fields):
        if not email:
            raise ValueError('Email field must be set')

        normalized_email = self.normalize_email(email)
        user = self.model(username=username, email=normalized_email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        if not extra_fields.get('is_staff'):
            raise ValueError('is_staff field must be set')
        if not extra_fields.get('is_superuser'):
            raise ValueError('is_superuser field must be set')
        self.create_user(username, email, password, **extra_fields)
