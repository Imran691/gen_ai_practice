# form package fastapi import FastAPI class
from fastapi import FastAPI

# create an instance of FastAPI class by calling its constructor
# app is the top-level FastAPI object that represents the whole web application

app : FastAPI = FastAPI()

# define rout's end point (set route) by using decorator & instance of FastAPI class that we created
# ("/") end point indicates home page
# We are calling its method get()
# the purpose of decorator is that when we use it, the function written immediately after it is integrated with it

#path decorator
@app.get("/")

# create a function for above created end point
# path function
def home() -> str:
    return "Hello World, Am here!"

# uvicorn package is used to run the srever of FastAPI
# To run the uvicorn server
# "uvicorn filename:objectname"
# "uvicorn hello:app"

# To automatically update the changes in our function return 
# "uvicorn hello:app --reload"

# to see the result at console 
# "http http://127.0.0.1:8000"        or
# "http localhost:8000"

# To see the docs at browser
# "http://127.0.0.1:8000/docs"