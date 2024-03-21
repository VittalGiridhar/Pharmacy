print ("Ragavendra")

from app import models
from app.database import engine
from fastapi import FastAPI
from app import Image2Text,dialogflow

models.Base.metadata.create_all(bind=engine)

application=FastAPI()
application.include_router(Image2Text.router)
application.include_router(dialogflow.router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(application, host="0.0.0.0", port=8080)