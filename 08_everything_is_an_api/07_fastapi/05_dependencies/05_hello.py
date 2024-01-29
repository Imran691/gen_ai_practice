from fastapi import FastAPI, Depends, HTTPException, status
from typing import Annotated

# Accessing the database and return the values based on their id's
# We will use blog & users dictionaries as data bases
blogs = {
    "1": "GenAI Blog",
    "2": "ML Blog",
    "3": "ML Bloگ",
}

users = {
    "8": "Imran",
    "9": "ALi",
}

# Title will be visible at "http://127.0.0.1:8000/docs"
app : FastAPI = FastAPI(title="Learn Dependency Injection")

# ceating dependency functions to search id's in blogs database
def get_blog_or_404(id:str):
    name = blogs.get(id)
    if not name:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog ID {id} not found")
    return name


@app.get("/blog/{id}")
def get_blog(blog_name: Annotated[str, Depends(get_blog_or_404)]):
    return {"Blog Name": blog_name}


# ceating dependency functions to search id's in users database
def get_user_or_404(id: str):
    name = users.get(id)
    if not name:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User ID {id} not found")
    return name

@app.get("/user/{id}")
def get_user(user_name: Annotated[str, Depends(get_user_or_404)]):
    return {"User Nanme": user_name}