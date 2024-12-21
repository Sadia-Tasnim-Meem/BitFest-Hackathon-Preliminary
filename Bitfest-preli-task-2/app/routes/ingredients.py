from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.models import Ingredient
from app.database import get_db

router = APIRouter()

@router.get("/")
def list_ingredients(db: Session = Depends(get_db)):
    return db.query(Ingredient).all()

@router.post("/")
def add_ingredient(name: str, quantity: float, unit: str, db: Session = Depends(get_db)):
    ingredient = Ingredient(name=name, quantity=quantity, unit=unit)
    db.add(ingredient)
    db.commit()
    db.refresh(ingredient)
    return ingredient
