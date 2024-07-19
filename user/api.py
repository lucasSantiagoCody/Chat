from .utils import register_request_validator
from ninja.errors import HttpError
from ninja.router import Router
from .schemas import UserSchema
from .models import User

router = Router()


@router.post("register/", response={201: dict})
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