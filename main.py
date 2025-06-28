import json

from fastapi import FastAPI

from database import SessionDep
from models import Category
from schema import CategoryForm

app = FastAPI()


@app.post("/category")
async def category_create(category: CategoryForm, session: SessionDep):
    new_category = Category(**dict(category))
    session.add(new_category)
    await session.commit()
    await session.refresh(new_category)
    return dict(new_category)

@app.put("/category/{category_id}")
async def update_category(category_id: int, Category: CategoryForm, session: SessionDep):
    new_category = session.get(Category, category_id)
    for key, value in Category(**dict(category).items()):
        setattr(new_category, key, value)
    await session.commit()
    await session.refresh(new_category)
    return new_category


@app.delete("/category")
async def delete_category(category_id:int, session: SessionDep):
    category = await session.get(Category, category_id)
    await session.delete(category)
    await session.commit()
    return {"message": "Category ochirildi"}


@app.get("/category/{id}", response_model=CategoryForm)
async def get_category(id: int, session: SessionDep):
    category = await session.get(Category, id)
    return category



# DELETE
# UPDATE
# LIST 
# DETAIL

