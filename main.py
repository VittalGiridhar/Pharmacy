print ("Ragavendra")

from app import models
from app.database import engine
from fastapi import FastAPI
from app import Image2Text,dialogflow
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from os import getenv 

models.Base.metadata.create_all(bind=engine)

application=FastAPI()
application.include_router(Image2Text.router)
application.include_router(dialogflow.router)



origins=["*"]
application.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
if __name__=="__main__":
    port=int(getenv("PORT",8000))
    uvicorn.run("app.api:app",host="0.0.0.0",port=port,reload=True)
