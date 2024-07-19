from django.contrib.auth import authenticate, login as auth_login
from .utils import register_request_validator
from ninja.errors import HttpError
from .schemas import LoginSchema
from ninja.router import Router
from .schemas import UserSchema
from .models import User

router = Router()

_LOGIN_BACKEND = 'django.contrib.auth.backends.ModelBackend'

@router.post('register/', response={201: dict})
def register(request, data:UserSchema):
    register_request_validator(data)
    try:
        user = User.objects.create_user(
            username=data.username,
            email=data.email,
            password=data.password
        )
        user.save()
        return {'message': 'registered user successfully'}
    except:
        raise HttpError(status_code=500, message='Internal server error')
    

@router.post('login/', response={200: dict, 401: str}, auth=None)
def login(request, data:LoginSchema):
    user = authenticate(backend=_LOGIN_BACKEND, **data.dict())
    if user and user.is_active:
        auth_login(request, user, backend=_LOGIN_BACKEND)
        return 200, {'message': 'Login successfully'}
    else:
        return 401, "Access denied"
