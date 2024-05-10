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
async def read_items_short(
    q: Annotated[str | None, Query(min_length=2, max_length=5)] = None
):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}

    if q:
        results.update({"q": q})
    
    return results


@app.get("/items_list/")
async def read_items_from_list(query: Annotated[list[str] | None, Query()] = None):
    
    query_items = {"query": query}
    
    return query_items


@app.get("/items_list_default/")
async def read_items_from_list_with_default(
    query: Annotated[list[str] | None, Query()] = ['Element 1', 'Element 2']
):
    
    query_items = {"query": query}
    
    return query_items