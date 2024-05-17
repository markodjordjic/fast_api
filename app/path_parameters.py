from fastapi import FastAPI

app = FastAPI()

fake_items_db = [
    {"item_name": "Foo"}, 
    {"item_name": "Bar"}, 
    {"item_name": "Baz"}
]


@app.get("/items/")
async def read_item(skip: int = 0, limit: int = 10):
    
    return fake_items_db[skip : skip + limit]

@app.get("/items/{item_id}")
async def read_item(item_id: str, query: str | None = None):

    if query is not None:
        
        return {"item_id": item_id, "query": query}

    return {"item_id": item_id}


@app.get("/users/{user_id}/items/{item_id}")
async def read_user_item(
    user_id: int, user_name: str, query: str | None = None, short: bool = False
):
    item = {"item_id": user_id, "owner_id": user_name}
    if query:
        item.update({"query": query})
    if short:
        item.update(
            {"short_name": user_name.upper()[0:3]}
        )
    return item