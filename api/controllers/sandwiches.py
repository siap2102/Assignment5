from sqlalchemy.orm import Session
from api.models import models, schemas

def create(db: Session, sandwich: schemas.SandwichCreate):
    db_item = models.Sandwich(**sandwich.dict())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

def read_all(db: Session):
    return db.query(models.Sandwich).all()

def read_one(db: Session, sandwich_id: int):
    return db.query(models.Sandwich).filter(models.Sandwich.id == sandwich_id).first()

def update(db: Session, sandwich_id: int, sandwich: schemas.SandwichUpdate):
    db_item = db.query(models.Sandwich).filter(models.Sandwich.id == sandwich_id)
    db_item.update(sandwich.dict(exclude_unset=True))
    db.commit()
    return db_item.first()

def delete(db: Session, sandwich_id: int):
    db_item = db.query(models.Sandwich).filter(models.Sandwich.id == sandwich_id)
    db_item.delete()
    db.commit()
    return
