from fastapi import APIRouter,Depends,HTTPException,status
from sqlalchemy.orm import Session
from .database import get_db
from . import models,utils,oauth2,schemas
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from random import randrange
from typing import List


router=APIRouter(
    tags=['consultation'],
    prefix='/consultation'
)


@router.post("/login",response_model=schemas.Token)
def login(login_credentials:OAuth2PasswordRequestForm=Depends(),db:Session=Depends(get_db)):
    data=db.query(models.Consultation).filter(models.Consultation.doctor_email==login_credentials.username).first() 
    if not data:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,details="invalid credential")
    
    verified_password=utils.verify(login_credentials.password,data.password)
    if not verified_password:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail="invalid credential")
    

    # return jwt token
    get_token=oauth2.create_token(data={"user_id":data.doctor_Id,"email":data.doctor_email})
    return {"access_token":get_token,"token_type":"bearer"}

@router.post("/signup")
def create_users(user:schemas.consultation_doctor_create,db:Session=Depends(get_db)):
    user=user.dict()
    data=db.query(models.Consultation).filter(models.Consultation.doctor_email==user['doctor_email']).all()
    print(data)
    if data:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="account already present")
    user['doctor_Id']=randrange(0,1000000)
    password=utils.hash_password(password=user["password"])
    user["password"]=password
    created_user=models.Consultation(**user) 
    db.add(created_user)
    db.commit()
    db.refresh(created_user)
    return created_user

@router.get("/viewall",response_model=List[schemas.all_doctor])
def view_all(db:Session=Depends(get_db)):
    data=db.query(models.Consultation).all()
    return [item.__dict__ for item in data]


@router.put("/update", response_model=schemas.all_doctor)
def update(input: schemas.update_timings, db: Session = Depends(get_db)):
    input_data = input.dict()
    consultation = db.query(models.Consultation).filter(models.Consultation.doctor_Id == input_data['doctor_Id']).first()
    if not consultation:
        raise HTTPException(status_code=status.HTTP_204_NO_CONTENT, detail="Doctor ID not available")
    
    update_data = {'timings': input_data['timings']}
    
    db.query(models.Consultation).filter(models.Consultation.doctor_Id == input_data['doctor_Id']).update(update_data, synchronize_session=False)
    db.commit()
    db.refresh(consultation)
    return consultation
    

