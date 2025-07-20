from sqlalchemy.orm import Session
from api.models import models, schemas

def create(db: Session, detail: schemas.OrderDetailCreate):
    db_item = models.OrderDetail(**detail.dict())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

def read_all(db: Session):
    return db.query(models.OrderDetail).all()

def read_one(db: Session, detail_id: int):
    return db.query(models.OrderDetail).filter(models.OrderDetail.id == detail_id).first()

def update(db: Session, detail_id: int, detail: schemas.OrderDetailUpdate):
    db_item = db.query(models.OrderDetail).filter(models.OrderDetail.id == detail_id)
    db_item.update(detail.dict(exclude_unset=True))
    db.commit()
    return db_item.first()

def delete(db: Session, detail_id: int):
    db_item = db.query(models.OrderDetail).filter(models.OrderDetail.id == detail_id)
    db_item.delete()
    db.commit()
    return
