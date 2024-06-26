from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
from app.sql import models, schemas, crud
from app.sql.session import make_session
from app.sql.database import engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.post("/users/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(make_session)):
    
    db_user = crud.get_user_by_email(db, email=user.email)
    
    if db_user:
        raise HTTPException(
            status_code=400, 
            detail="Email already registered."
        )
    
    return crud.create_user(db=db, user=user)


@app.post("/delete_user/")
def delete_user(user: schemas.UserCreate, db: Session = Depends(make_session)):
    
    db_user = crud.get_user_by_email(db, email=user.email)
    
    if db_user:
        crud.delete_user(db=db, user=db_user)
        
    else:
        raise HTTPException(status_code=400, detail="Item not found.")
    
    return f"User {db_user.email} deleted."

@app.get("/user/{user_id}", response_model=schemas.User)
def read_user(user_id: int, db: Session = Depends(make_session)):
    
    db_user = crud.get_user(db, user_id=user_id)
    
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    
    return db_user


@app.get("/users/", response_model=list[schemas.User])
def read_users(skip: int = 0, 
               limit: int = 100, 
               db: Session = Depends(make_session)):
    
    users = crud.get_users(db, skip=skip, limit=limit)
     
    return users


@app.post("/users/{user_id}/item/", response_model=schemas.Item)
def create_item_for_user(user_id: int, 
                         item: schemas.ItemCreate, 
                         db: Session = Depends(make_session)):
    
    return crud.create_user_item(db=db, item=item, user_id=user_id)


@app.get("/items/", response_model=list[schemas.Item])
def read_items(skip: int = 0, 
               limit: int = 100, 
               db: Session = Depends(make_session)):
    
    items = crud.get_items(db, skip=skip, limit=limit)
    
    return items