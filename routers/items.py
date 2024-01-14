from fastapi import Depends
from fastapi import APIRouter
from call_db import get_db
from models import schemas
from sqlalchemy.orm import Session

from services import item_services
router = APIRouter()

@router.get("/items/", response_model=list[schemas.Item])
def read_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    items = item_services.get_items(db, skip=skip, limit=limit)
    return items

@router.post("/items/", response_model=schemas.Item)
def create_item(item: schemas.ItemCreate, db: Session = Depends(get_db)):
    return item_services.create_item(db=db, item=item)
