from fastapi import FastAPI
from pydantic import BaseModel


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None

article_specification = {
    "name": "Surfing Board",
    "description": "Large surfing board for open water.",
    "price": 499.999,
    "tax": 11.00
}

item = Item(**article_specification)

app = FastAPI()


@app.post("/items/")
async def create_item(item: Item = item):
    
    return item


@app.post("/items_wh_tax/")
async def create_item_wh_tax(item: Item = item):
    item_dict = item.model_dump()
    if item.tax is not None:
        price_with_tax = item.price + item.tax
        item_dict.update({"price_with_tax": price_with_tax})
    
    return item_dict


@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item = item):

    return {"item_id": item_id, **item.model_dump()}


@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item = item, q: str | None = None):
    
    result = {"item_id": item_id, **item.model_dump()}
    
    if q:
        result.update({"q": q})
    
    return result