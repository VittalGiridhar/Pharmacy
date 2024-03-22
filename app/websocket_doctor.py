from fastapi import WebSocket, APIRouter
from typing import Dict


router = APIRouter(tags=['websocket'])

user_websockets: Dict[str, WebSocket] = {}

@router.websocket("/ws/{user_id}")
async def websocket_endpoint(user_id: str, websocket: WebSocket):
    await websocket.accept()
    user_websockets[user_id] = websocket
    try:
        while True:
            message = await websocket.receive_text()
            recipient_id, message = message.split(":", 1)
            print(recipient_id)
            if recipient_id in user_websockets:
                recipient_ws = user_websockets[recipient_id]
                await recipient_ws.send_text(f"From User {user_id}: {message}")
            else:
                await websocket.send_text(f"User {recipient_id} is not connected.")
    except :
        del user_websockets[user_id]

