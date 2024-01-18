from typing import Annotated

from fastapi import APIRouter
from fastapi import Depends
from sqlalchemy.orm import Session


from call_db import get_db
from app.models import schemas
from app.repositories.item_repository import ItemRepository
from app.services.users_services import get_current_active_user

router = APIRouter()


@router.get("/items/", response_model=list[schemas.Item])

def read_items(current_user: Annotated[schemas.User,Depends(get_current_active_user)], skip: int = 0,limit: int = 100,db: Session = Depends(get_db)):
    item_repository=ItemRepository(db=db)
    items = item_repository.list(skip=skip, limit=limit)
    return items


@router.post("/items/", response_model=schemas.Item)
def create_item(current_user: Annotated[schemas.User, Depends(get_current_active_user)], item: schemas.ItemCreateOrUpdate, db: Session = Depends(get_db)):
    item_repository=ItemRepository(db=db)
    return item_repository.create( item=item)

@router.patch("/items/{id}", response_model=schemas.Item)
def create_item(current_user: Annotated[schemas.User, Depends(get_current_active_user)],id:int, item: schemas.ItemCreateOrUpdate, db: Session = Depends(get_db)):
    item_repository=ItemRepository(db=db)
    return item_repository.update(id=id, item=item)
