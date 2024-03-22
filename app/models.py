from .database import Base
from sqlalchemy import Column,Integer,String,VARCHAR,ForeignKey,Float


class Pharmacy(Base):
    __tablename__="Pharmacy_Table"
    Pharmacy_ID=Column("Pharmacy_ID",Integer,primary_key=True,nullable=False,unique=True)
    Pharmacy_name=Column("Pharmacy_name",String,nullable=False)
    email_ID=Column("email_ID",String,nullable=False,unique=True)
    password=Column("Password",String,nullable=False)
    Pharmacy_mobileNo=Column("mobile_number",Integer,nullable=False)
    Pharmacy_address=Column("address",String,unique=True,nullable=False)
    Pharmacy_location=Column("location",VARCHAR,unique=True,nullable=False)
    Drug_License=Column("Drug_License",VARCHAR,nullable=False)
    GST_Registration_Certificate=Column("GST_Registration_Certificate",VARCHAR,nullable=False)
    Shops_and_Establishment_Act_registration_Certificate =Column("Shops_and_Establishment_Act_registration_Certificate",VARCHAR,nullable=False)
    Trade_License =Column("Trade_License",VARCHAR,nullable=False)
    FSSAI_License =Column("FSSAI_License",VARCHAR,nullable=False)
    Fire_Safety_Certificate=Column("Fire_Safety_Certificate",VARCHAR,nullable=False)
    Pollution_Control_Board_NOC =Column("Pollution_Control_Board_NOC",VARCHAR,nullable=True,server_default="No image")
    Business_Registration_Documents=Column("Business_Registration_Documents",VARCHAR,nullable=False)
    Medical_Council_Registration=Column("Medical_Council_Registration",VARCHAR,nullable=True,server_default="No image")
    Signage_License=Column("Signage_License",VARCHAR,nullable=True,server_default="No image")
    Status=Column("Status",String,nullable=False,server_default="unverified")

class Medicine_for_Admin(Base):
    __tablename__="Med_for_Admin"
    Medicine_ID=Column("Medicine_ID",Integer,primary_key=True,nullable=False)
    medicine_name=Column("medicine_name",String,unique=True,nullable=False)
    status=Column("status",String,nullable=False,server_default="unverified")
    price_for_1_strip=Column("price_for_1_strip",Float,nullable=False,server_default="0.0")

class Consultation(Base):
    __tablename__="Consultation"
    doctor_Id=Column("doctor_Id",Integer,primary_key=True,nullable=False)
    doctor_username=Column("doctor_username",String,nullable=False)
    doctor_email=Column("doctor_email",String,unique=True,nullable=False)
    password=Column("password",String,nullable=False)
    timings=Column("timings",String,unique=True,server_default="0")  
