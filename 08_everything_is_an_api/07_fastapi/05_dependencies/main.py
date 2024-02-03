from fastapi import FastAPI, Depends, HTTPException, status
from typing import Annotated

# Sample data base
development_db = ["DB for development"]

def get_db_session():
    return development_db

app : FastAPI = FastAPI()   

@app.get("/add-item")
def add_item(item: str, db: Annotated[list, Depends(get_db_session)]):
    db.append(item)
    print(db)
    return {"message": f"Item {item} added to the database"}#, "complete-database": db}