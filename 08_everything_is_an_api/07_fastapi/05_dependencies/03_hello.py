from fastapi import FastAPI, Depends, Query
from typing import Annotated

app : FastAPI = FastAPI()

# Function to check if username and password are provided to proceed further
# For user authentication
def dep_check(username: str = Query(None), password: str= Query(None)):
    if not username or not password:
        raise

# Dependency function can be passed as parameter in our custom function as we did in previous examples
# Or we can pass the dependency in the route directly as we did here
# If dependency function is not returning anything, we can pass it in URL path
@app.get("/login", dependencies=[Depends(dep_check)])
def login():
    return True