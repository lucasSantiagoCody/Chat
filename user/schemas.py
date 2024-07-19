from ninja.schema import Schema
from ninja import ModelSchema
from .models import User

class UserSchema(ModelSchema):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']

class LoginSchema(Schema):
    email: str
    password: str