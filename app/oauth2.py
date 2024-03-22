from fastapi import Depends, HTTPException,status
from jose import JWTError,jwt
from datetime import datetime,timedelta

from . import schemas,models
from .database import get_db
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from app.config import settings

oauth2_scheme=OAuth2PasswordBearer(tokenUrl="login")

SECRET_KEY="jgjsdgviugiqu98349834983kjjwr9839834oihiohr9874ou9098y34giug3498u9r"
ALGORITHM="HS256"
EXPIRE_TIME=60

def create_token(data:dict):
    to_encode=data.copy()
    expire_duration=datetime.utcnow() + timedelta(minutes=EXPIRE_TIME)
    to_encode.update({"exp":expire_duration})

    token=jwt.encode(to_encode,SECRET_KEY,algorithm=ALGORITHM)
    return token

def verify_token(token:schemas.Token,credential_exception):
    try:
        to_decode=token
        decoded_value=jwt.decode(to_decode,SECRET_KEY,algorithms=[ALGORITHM])
        id: str=decoded_value.get("user_id")
        if id is None:
            raise credential_exception
        token_data=schemas.Token_data(id=str(id))
    except JWTError:
        raise credential_exception
    return token_data
        
def get_current_user(token:str=Depends(oauth2_scheme),db:Session=Depends(get_db)):
    credentials_exception = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="Could not validate credentials"
                                          ,headers={"WWW-Authenticate": "Bearer"},)
    get_data= verify_token(token,credentials_exception)
    user=db.query(models.Consultation).filter(models.Consultation.doctor_Id==get_data.id).first()
    return user 