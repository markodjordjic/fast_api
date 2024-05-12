from typing import Annotated

from fastapi import FastAPI, Path
from pydantic import BaseModel

class Item(BaseModel):
    name: str
    description: str | None = None
    base_price: float
    tax: float | None = None

class TaggedItem(BaseModel):
    name: str
    description: str | None = None
    base_price: float
    tax: float | None = None
    tags: list[str] = []

article_specification = {
    'name': 'Cake mould',
    'description': '8" diameter mould from metal.',
    'base_price': 499.00,
    'tax': 18.0
}

tagged_article_specification = {
    'name': 'Cake mould',
    'description': '8" diameter mould from metal.',
    'base_price': 499.00,
    'tax': 18.0,
    'tags': ['discount', 'standard offer']
}



article = Item(**article_specification)
tagged_article = TaggedItem(**tagged_article_specification)


app = FastAPI()

@app.put("/update_item/{item_id}")
async def update_item(
    item_id: Annotated[int, Path(title="The ID of the item to get", ge=0, le=1000)],
    q: str | None = None,
    item: Item | None = article,
):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    if item:
        results.update({"item": item})
    
    return results


@app.put("/update_tagged_item/{item_id}")
async def update_item(
    item_id: Annotated[
        int, 
        Path(title="The ID of the item to get", ge=0, le=1000)
    ],
    q: str | None = None,
    item: Item | None = tagged_article
):
    results = {"item_id": item_id}
    
    if q:
        results.update({"q": q})
    if item:
        results.update({"item": item})
    
    return results