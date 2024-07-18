from ninja import NinjaAPI
from user.api import router as users_router

api = NinjaAPI()

api.add_router('user/', users_router)

