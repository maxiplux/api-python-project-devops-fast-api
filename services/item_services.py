from sqlalchemy.orm import Session
from models import schemas, core

def get_items(db: Session, skip: int = 0, limit: int = 100):
    return db.query(core.Item).offset(skip).limit(limit).all()


def create_item(db: Session, item: schemas.ItemCreate):
    db_item = core.Item(**item.dict())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item