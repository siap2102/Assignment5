from sqlalchemy.orm import Session
from api.models import models, schemas

def create(db: Session, resource: schemas.ResourceCreate):
    db_item = models.Resource(**resource.dict())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

def read_all(db: Session):
    return db.query(models.Resource).all()

def read_one(db: Session, resource_id: int):
    return db.query(models.Resource).filter(models.Resource.id == resource_id).first()

def update(db: Session, resource_id: int, resource: schemas.ResourceUpdate):
    db_item = db.query(models.Resource).filter(models.Resource.id == resource_id)
    db_item.update(resource.dict(exclude_unset=True))
    db.commit()
    return db_item.first()

def delete(db: Session, resource_id: int):
    db_item = db.query(models.Resource).filter(models.Resource.id == resource_id)
    db_item.delete()
    db.commit()
    return

