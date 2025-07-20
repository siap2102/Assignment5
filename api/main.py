from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

from api.dependencies.database import get_db, engine
from api.models import models, schemas
from api.controllers import sandwiches, resources, recipes, order_details

# Create database tables
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# -----------------------------
# Sandwich Routes
# -----------------------------
@app.post("/sandwiches/", response_model=schemas.Sandwich, tags=["Sandwiches"])
def create_sandwich(item: schemas.SandwichCreate, db: Session = Depends(get_db)):
    return sandwiches.create(db, item)

@app.get("/sandwiches/", response_model=list[schemas.Sandwich], tags=["Sandwiches"])
def read_sandwiches(db: Session = Depends(get_db)):
    return sandwiches.read_all(db)

@app.get("/sandwiches/{item_id}", response_model=schemas.Sandwich, tags=["Sandwiches"])
def read_sandwich(item_id: int, db: Session = Depends(get_db)):
    result = sandwiches.read_one(db, item_id)
    if not result:
        raise HTTPException(status_code=404, detail="Sandwich not found")
    return result

@app.put("/sandwiches/{item_id}", response_model=schemas.Sandwich, tags=["Sandwiches"])
def update_sandwich(item_id: int, item: schemas.SandwichUpdate, db: Session = Depends(get_db)):
    return sandwiches.update(db, item_id, item)

@app.delete("/sandwiches/{item_id}", status_code=204, tags=["Sandwiches"])
def delete_sandwich(item_id: int, db: Session = Depends(get_db)):
    return sandwiches.delete(db, item_id)


# -----------------------------
# Resource Routes
# -----------------------------
@app.post("/resources/", response_model=schemas.Resource, tags=["Resources"])
def create_resource(item: schemas.ResourceCreate, db: Session = Depends(get_db)):
    return resources.create(db, item)

@app.get("/resources/", response_model=list[schemas.Resource], tags=["Resources"])
def read_resources(db: Session = Depends(get_db)):
    return resources.read_all(db)

@app.get("/resources/{item_id}", response_model=schemas.Resource, tags=["Resources"])
def read_resource(item_id: int, db: Session = Depends(get_db)):
    result = resources.read_one(db, item_id)
    if not result:
        raise HTTPException(status_code=404, detail="Resource not found")
    return result

@app.put("/resources/{item_id}", response_model=schemas.Resource, tags=["Resources"])
def update_resource(item_id: int, item: schemas.ResourceUpdate, db: Session = Depends(get_db)):
    return resources.update(db, item_id, item)

@app.delete("/resources/{item_id}", status_code=204, tags=["Resources"])
def delete_resource(item_id: int, db: Session = Depends(get_db)):
    return resources.delete(db, item_id)


# -----------------------------
# Recipe Routes
# -----------------------------
@app.post("/recipes/", response_model=schemas.Recipe, tags=["Recipes"])
def create_recipe(item: schemas.RecipeCreate, db: Session = Depends(get_db)):
    return recipes.create(db, item)

@app.get("/recipes/", response_model=list[schemas.Recipe], tags=["Recipes"])
def read_recipes(db: Session = Depends(get_db)):
    return recipes.read_all(db)

@app.get("/recipes/{item_id}", response_model=schemas.Recipe, tags=["Recipes"])
def read_recipe(item_id: int, db: Session = Depends(get_db)):
    result = recipes.read_one(db, item_id)
    if not result:
        raise HTTPException(status_code=404, detail="Recipe not found")
    return result

@app.put("/recipes/{item_id}", response_model=schemas.Recipe, tags=["Recipes"])
def update_recipe(item_id: int, item: schemas.RecipeUpdate, db: Session = Depends(get_db)):
    return recipes.update(db, item_id, item)

@app.delete("/recipes/{item_id}", status_code=204, tags=["Recipes"])
def delete_recipe(item_id: int, db: Session = Depends(get_db)):
    return recipes.delete(db, item_id)


# -----------------------------
# Order Details Routes
# -----------------------------
@app.post("/order-details/", response_model=schemas.OrderDetail, tags=["Order Details"])
def create_order_detail(item: schemas.OrderDetailCreate, db: Session = Depends(get_db)):
    return order_details.create(db, item)

@app.get("/order-details/", response_model=list[schemas.OrderDetail], tags=["Order Details"])
def read_order_details(db: Session = Depends(get_db)):
    return order_details.read_all(db)

@app.get("/order-details/{item_id}", response_model=schemas.OrderDetail, tags=["Order Details"])
def read_order_detail(item_id: int, db: Session = Depends(get_db)):
    result = order_details.read_one(db, item_id)
    if not result:
        raise HTTPException(status_code=404, detail="Order detail not found")
    return result

@app.put("/order-details/{item_id}", response_model=schemas.OrderDetail, tags=["Order Details"])
def update_order_detail(item_id: int, item: schemas.OrderDetailUpdate, db: Session = Depends(get_db)):
    return order_details.update(db, item_id, item)

@app.delete("/order-details/{item_id}", status_code=204, tags=["Order Details"])
def delete_order_detail(item_id: int, db: Session = Depends(get_db)):
    return order_details.delete(db, item_id)
