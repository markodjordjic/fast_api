from app.sql.database import SessionLocal


def make_session():

    db = SessionLocal()
    
    try:
        yield db
    
    finally:
        db.close()