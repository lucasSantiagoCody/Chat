from ninja import NinjaAPI
from user.api import router as user_router
from chat.api import router as chat_router


api = NinjaAPI()

api.add_router('user/', user_router)
api.add_router('chat/', chat_router)
