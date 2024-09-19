from fastapi import FastAPI, Depends, HTTPException, status
from database import get_db, create_db_and_tables
from model import Brand, BrandUpdate

from sqlmodel import Session


app = FastAPI()


create_db_and_tables()


@app.post("/create-brand")
async def create_brand(brand: Brand, db: Session = Depends(get_db)):
    db.add(brand)
    db.commit()
    db.refresh(brand)
    return brand

@app.get("/get-brand")
async def get_brand(db:Session = Depends(get_db)):
    brand = db.query(Brand).all()
    return brand

@app.get("/get-brand/{id}")
async def get_brand_id(id: int, db: Session = Depends(get_db)):
    brand = db.query(Brand).filter(Brand.id == id).first()

    return brand


@app.put("/update-brand/{id}")
async def update_brand(id: int, brand_update: BrandUpdate, db: Session = Depends(get_db)):
    # Retrieve the brand
    brand = db.query(Brand).filter(Brand.id == id).first()

    # Create a dictionary of the fields to update
    updates = {
        "name": brand_update.name,
        "description": brand_update.description,
        "image_url": brand_update.image_url
    }

    # Update only the fields that are not None
    for field, value in updates.items():
        if value is not None:
            setattr(brand, field, value)
    # Commit the changes
    db.commit()
    db.refresh(brand)

    return brand


@app.delete("/delete-brand/{id}")
async def delete_brand(id: int, db: Session = Depends(get_db)):
    # Retrieve the brand
    brand = db.query(Brand).filter(Brand.id == id).first()

    if not brand:
        raise HTTPException(status_code=404, detail="Brand not found")

    # Delete the brand
    db.delete(brand)
    db.commit()

    return {"detail": "Brand deleted successfully"}

