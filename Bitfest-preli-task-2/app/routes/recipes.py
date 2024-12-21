from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.models import Recipe
from app.database import get_db

router = APIRouter()

@router.get("/")
def list_recipes(db: Session = Depends(get_db)):
    return db.query(Recipe).all()

@router.post("/")
def add_recipe(title: str, ingredients: dict, instructions: str, db: Session = Depends(get_db)):
    recipe = Recipe(title=title, ingredients=ingredients, instructions=instructions)
    db.add(recipe)
    db.commit()
    db.refresh(recipe)
    return recipe
