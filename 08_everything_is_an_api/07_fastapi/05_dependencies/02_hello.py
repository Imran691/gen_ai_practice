from fastapi import FastAPI, Depends, Query
from typing import Annotated

app : FastAPI = FastAPI()

def login(username: str = Query(None), password: str = Query(None)):
    if(username == "Imran" and password == "1234"):
        return {"message": "Login Successful"}
    else: 
        return {"mssage": "Login Failed"}
    
@app.get("/login")
# Annotated calss from typing to define the type & inject dependency function
def login_api(result : Annotated[dict, Depends(login)]):
    return result