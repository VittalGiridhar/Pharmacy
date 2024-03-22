import cv2
import numpy as np
import json
import base64
from fastapi import APIRouter, WebSocket
from typing import Dict

router = APIRouter(
    prefix='/image',
    tags=["Text from Image"]
)

class ImgExt:
    def __init__(self):
        self.websocket_connections: Dict[int, WebSocket] = {}

    async def accept_connection(self, user_Id: int, websocket: WebSocket):
        await websocket.accept()
        self.websocket_connections[user_Id] = websocket

    async def close_connection(self, user_Id: int):
        if user_Id in self.websocket_connections:
            del self.websocket_connections[user_Id]

    async def send_message(self, user_Id: int, websocket: WebSocket, message: str):
        if user_Id in self.websocket_connections:
            await self.websocket_connections[user_Id].send_text(message)

    async def receive_message(self, user_Id, websocket: WebSocket):
        if user_Id in self.websocket_connections:
            img = await websocket.receive_text()
            return img

manager = ImgExt()

@router.websocket("/ws/{user_Id}")
async def imageExtraction(websocket: WebSocket, user_Id: int):
    await manager.accept_connection(user_Id=user_Id, websocket=websocket)
    try:
        json_data = await manager.receive_message(user_Id=user_Id, websocket=websocket)
        lst = json.loads(json_data)

        
        width = 240
        height = 320 
        img = np.zeros((height, width, 3), dtype=np.uint8)
        index = 0
        for y in range(height):
            for x in range(width):
                img[y, x] = lst[index]
                index += 1

        cv2.imwrite('reconstructed_image.jpg', img)

        x=cv2.imread('page.jpg')
        text=imgExt()
        await manager.send_message(user_Id=user_Id, websocket=websocket, message=text)
    except json.JSONDecodeError as e:
        print("Error decoding JSON:", e)
    except IndexError as e:
        print("Index out of range:", e)
    except cv2.error as e:
        print("OpenCV error:", e)
    except Exception as e:
        print("Unhandled exception:", e)
        raise e
    

import pytesseract
def imgExt():    
    img=cv2.imread("reconstructed_image.jpg",0)
    thr=cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,21,2)
    cv2.imshow("threshold image",thr)
    k=cv2.waitKey(0)
    if k==ord('q'):
        cv2.destroyAllWindows()
    
    text = pytesseract.image_to_string(thr)
    print(text)
    return text
