from fastapi import FastAPI, Depends, Query

app : FastAPI = FastAPI()

# The dependency function 
# It provides us Modularity
# Once defined, we can use it with multiple URL paths / routes
# We don't need to define it again and again

# name and password will be provided as query parameter (url/user?name=Imran&password=1234)
# beacuse we are using Query class from fastapi
def user_dep(name : str = Query(None), password : str = Query(None)):
    return {"name" : name, "valid": True}

# The path function / web endpoint

@app.get("/user")
# user:dict will be returned by invoking dependency function when we hit the URL path
def get_user(user: dict = Depends(user_dep)):
    return user