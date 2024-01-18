from sqlalchemy.orm import Session

from app.models import schemas, core
from call_db import get_db

from fastapi import Depends
class ItemRepository:
    db: Session
    def __init__(self, db: Session ) -> None:
        self.db = db


    def list(self, skip: int = 0, limit: int = 100)-> list[core.Item]:
        return self.db.query(core.Item).offset(skip).limit(limit).all()

    def create(self, item: schemas.ItemCreateOrUpdate)-> core.Item:
        db_item = core.Item(**item.dict())
        self.db.add(db_item)
        self.db.commit()
        self.db.refresh(db_item)
        return db_item

    def update(self, id: int, item: schemas.ItemCreateOrUpdate) -> core.Item:
        item.id = id
        db_item = self.db.query(core.Item).filter(core.Item.id == id).first()
        db_item.title = item.title
        db_item.description = item.description


        self.db.merge(db_item)
        self.db.commit()

        self.db.commit()
        return item

    def delete(self, book: core.Item) -> None:
        self.db.delete(book)
        self.db.commit()
        self.db.flush()
    ## implement update

