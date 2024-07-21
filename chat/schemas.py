from ninja import Schema

class RoomSchema(Schema):
    name: str

class MessageRoom(Schema):
    room_id: int
    content: str
    