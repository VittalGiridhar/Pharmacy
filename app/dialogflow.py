from fastapi import FastAPI,APIRouter,Depends
from .database import get_db
from sqlalchemy.orm import Session
from . import models
from google.cloud import dialogflow

router=APIRouter(
    prefix="/dialogflow",
    tags=['dialogflow'],
)
lst=[]
@router.get("/")
def dialogflow(db:Session=Depends(get_db)):
    data=db.query(models.Medicine_for_Admin).all()
    print(data)
    for i in data:
        print(i.Medicine_name)
    # for item in data:
    #     x=item['medicine_name']
    #     lst.append(x)
    #     print(lst)
    return data 