from sqlalchemy.orm import Session
from api.models import models, schemas

def create(db: Session, recipe: schemas.RecipeCreate):
    db_item = models.Recipe(**recipe.dict())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

def read_all(db: Session):
    return db.query(models.Recipe).all()

def read_one(db: Session, recipe_id: int):
    return db.query(models.Recipe).filter(models.Recipe.id == recipe_id).first()

def update(db: Session, recipe_id: int, recipe: schemas.RecipeUpdate):
    db_item = db.query(models.Recipe).filter(models.Recipe.id == recipe_id)
    db_item.update(recipe.dict(exclude_unset=True))
    db.commit()
    return db_item.first()

def delete(db: Session, recipe_id: int):
    db_item = db.query(models.Recipe).filter(models.Recipe.id == recipe_id)
    db_item.delete()
    db.commit()
    return
