from fastapi import FastAPI
from pydantic import BaseModel


class System(BaseModel):
    name: str
    pre_processor: str | None
    predictor: str
    post_processor: str | None

system_specification_values = {
    "name": "Linear Regression",
    "pre_processor": "StandardScaler",
    "predictor": "LinearRegression",
    "post_processor": None
}

system = System(**system_specification_values)

app = FastAPI()


@app.get("/")
async def root():
    """Path function

    """    
    
    return {"message": "Hello wild"}

@app.get("/items/{item}")
async def path_parameter(item_id):
    """Path function

    """    
    
    return {"message": item_id}

@app.get("/items/{item_id}")
async def path_parameter_wh_type(item_id: int):
    """Path function

    Parameters
    ----------
    item_id : int
        _description_

    Returns
    -------
    _type_
        _description_
    """
    
    return {"item_id": item_id}


@app.get("/models/{system_specification}")
async def get_model_specification(system_specification: System):

    if system_specification.pre_processor is not None:

        pre_status = f'System: {system_specification.name} requires pre-processor {system_specification.pre_processor}'

    if system_specification.post_processor is not None:

        post_status = f'System: {system_specification.name} requires post-processor {system_specification.pre_processor}'


    return {"report": pre_status + r'\n' + post_status}


@app.get("/files/{file_path:path}")
async def read_file(file_path: str):

    return {"file_path": file_path}