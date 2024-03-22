from fastapi import APIRouter, Depends
from .database import get_db
from sqlalchemy.orm import Session
from . import models,schemas
from random import randrange

#   pharmacy-API
router=APIRouter(
    prefix="/MediceAdmin",
    tags=['MediceAdmin']
)

@router.get("/")
def Med_Admin_get(db:Session=Depends(get_db)):
    data=db.query(models.Medicine_for_Admin).all()
    return data

@router.post("/")
def Med_Admin_post(createPost:schemas.Med_Admin_create,db:Session=Depends(get_db)):
    new_post=createPost.dict()
    new_post["Medicine_ID"]=randrange(0,10000000)
    new_data=models.Medicine_for_Admin(**new_post)
    db.add(new_data)
    db.commit()
    db.refresh(new_data)
    return new_data


