from typing import Annotated

from fastapi import FastAPI, Path, Query

app = FastAPI()

@app.get("/read_items/{item_id}")
async def read_items(
    item_id: Annotated[int, Path(title="The ID of the item to get")],
    q: Annotated[str | None, Query(alias="item-query")] = None,
):
    results = {"item_id": item_id}

    if q:
        results.update({"q": q})
    
    return results


@app.get("/read_items_ge/{item_id}")
async def read_items_ge(
    item_id: Annotated[int, Path(title="The ID of the item to get", ge=50)], 
    q: str
):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})

    return results