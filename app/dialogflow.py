from fastapi import FastAPI, APIRouter, Depends
from .database import get_db
from sqlalchemy.orm import Session
from . import models


router = APIRouter(
    prefix="/dialogflow",
    tags=['dialogflow'],
)

# dialogflow_client = dialogflow_v2.EntityTypesClient()

@router.get("/")
def dialogflow(db: Session = Depends(get_db)):
    data = db.query(models.Medicine_for_Admin).all()
    # entity_values = []
    # for item in data:
    #     entity_values.append(item.Medicine_name)
    # entity_type_path = dialogflow_client.entity_type_path("hedix-nosa", "Asia/Almaty", "110549af-0b86-4f5d-a8e5-3af030eb56e0")
    # entities = [ {"value": value} for value in entity_values]
    # entity = {
    #     "display_name": "MedicineNameEntity", 
    #     "entities": entities
    # }
    # response = dialogflow_client.batch_create_entities(parent=entity_type_path, entities=[entity])
    return data
