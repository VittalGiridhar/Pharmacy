from pydantic import BaseModel,EmailStr
from typing import Optional
class Med_Admin_create(BaseModel):
    medicine_name:str
    price_for_1_strip:int
    status:str

class Token_data(BaseModel):
    id:Optional[str]=None

class Token(BaseModel):
    access_token:str
    token_type:str

class consultation_doctor_create(BaseModel):
    doctor_email:EmailStr
    doctor_username:str
    password:str

class all_doctor(BaseModel):
    doctor_Id:int
    doctor_username:str
    doctor_email:str
    timings:str

class update_timings(BaseModel):
    doctor_Id:int
    timings:str
    