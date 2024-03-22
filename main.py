print ("Ragavendra")

from app import Med_Admin_API, models
from app.database import engine
from fastapi import FastAPI
from app import Image2Text,dialogflow,Med_Admin_API,consultation_API,websocket_doctor

models.Base.metadata.create_all(bind=engine)

application=FastAPI()
application.include_router(Image2Text.router)
application.include_router(dialogflow.router)
application.include_router(Med_Admin_API.router)
application.include_router(consultation_API.router)
application.include_router(websocket_doctor.router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(application, host="0.0.0.0", port=8000)