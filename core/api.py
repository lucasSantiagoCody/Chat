from ninja import NinjaAPI
from user.api import router as users_router
from chat.api import router as chat_routers


api = NinjaAPI()

api.add_router('user/', users_router)
api.add_router('chat/', chat_routers)
