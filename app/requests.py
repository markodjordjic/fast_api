from fastapi import FastAPI, Body
from pydantic import BaseModel, Field
from typing import Annotated

app = FastAPI()

class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "name": "Foo",
                    "description": "A very nice Item",
                    "price": 35.4,
                    "tax": 3.2,
                }
            ]
        }
    }

class ItemWhField(BaseModel):
    name: str = Field(
        examples=["Chips"]
    )
    description: str | None = Field(
        default=None, 
        examples=["Potato chips, salted"]
    )
    price: float = Field(examples=[99.0])
    tax: float | None = Field(
        default=None, examples=[11.0]
    )


@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item):

    results = {"item_id": item_id, "item": item}
    
    return results

@app.put("/items_wh_field/{item_id}")
async def update_item_wh_field(item_id: int, item: ItemWhField):
    
    results = {"item_id": item_id, "item": item}
    
    return results

@app.put("/items_wh_examples/{item_id}")
async def update_item_wh_examples(
    *,
    item_id: int,
    item: Annotated[
        Item,
        Body(
            openapi_examples={
                "normal": {
                    "summary": "A normal example",
                    "description": "A **normal** item works correctly.",
                    "value": {
                        "name": "Foo",
                        "description": "A very nice Item",
                        "price": 35.4,
                        "tax": 3.2,
                    },
                },
                "converted": {
                    "summary": "An example with converted data",
                    "description": "FastAPI can convert price `strings` to actual `numbers` automatically",
                    "value": {
                        "name": "Bar",
                        "price": "35.4",
                    },
                },
                "invalid": {
                    "summary": "Invalid data is rejected with an error",
                    "value": {
                        "name": "Baz",
                        "price": "thirty five point four",
                    },
                },
            },
        ),
    ],
):

    results = {"item_id": item_id, "item": item}

    return results