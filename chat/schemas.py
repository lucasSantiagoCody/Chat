from ninja import Schema

class RoomSchema:
    name: str

class MessageRoom:
    room_id: int
    content: str
    