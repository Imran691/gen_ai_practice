from fastapi import FastAPI, Depends, Query

app : FastAPI = FastAPI()   

def login(username: str = Query(None), password: str = Query(None)):
    if(username=="admin" and password=="admin"):
        return {"message": "valid user"}
    else:
        return {"invalid username or password"}

@app.get("/login")
# dependancy function is invoked by passing as dependency injection
def login_api(result = Depends(login)):
    return result

# If we don't use Depends calss the syntex of the programm would be as folows
# def login(username: str, password:str):
#     if(username=="admin" and password=="admin"):    
#         return {"message": "valid user"}
#     else:   
#         return {"invalid username or password"}
    
# @app.get("/login")
# def login_api(username, password ):
#     # manually invoking login function
#     result  = login(username, password) 
#     return result