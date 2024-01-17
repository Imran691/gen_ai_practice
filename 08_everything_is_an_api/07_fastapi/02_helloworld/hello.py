# form package fastapi import FastAPI class
from fastapi import FastAPI

# create an instance of FastAPI class by calling its constructor
app : FastAPI = FastAPI()

# define rout's end point by using decorator & instance of FastAPI class that we created
# ("/") end point indicates home page
@app.get("/")

# create a function for above created end point
def home() -> str:
    return "Hello World, abc"

# To run the uvicorn server
# "uvicorn filename:objectname"
# "uvcorn hello:app"

# To update the changes in our function return 
# "uvicorn hello:app --reload"

# to see the result at console 
# "http http://127.0.0.1:8000"        or
# "http localhost:8000"

# To see the docs at browser
# "http://127.0.0.1:8000/docs"


