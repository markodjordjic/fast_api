from typing import Annotated
from fastapi import FastAPI, Query

app = FastAPI()

@app.get("/items/")
async def read_items(q: str | None = None):
    
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    
    if q:
        results.update({"q": q})
    
    return results

@app.get("/items_short/")
async def read_items_short(q: Annotated[str | None, Query(max_length=5)] = None):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    
    return results