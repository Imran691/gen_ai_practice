from fastapi import FastAPI, Depends, HTTPException, status
from typing import Annotated


blogs = {
    "1": "GenAI Blog",
    "2": "ML Blog",
    "3": "ML Bloگ",
}

users = {
    "8": "Imran",
    "9": "ALi",
}

# This class will be used to create depdendency object
class GetObjectOr404():
    def __init__(self, model) -> None:
        self.model = model  
    
    # To make the instances callable
    def __call__(self, id:str):
        obj = self.model.get(id)
        if not obj:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Object ID {id} not found")    
        return obj

app : FastAPI = FastAPI(title="Learn Dependency Injection")

# blog_depdency instance of above created call
blog_dependency = GetObjectOr404(blogs)

@app.get("/blog/{id}")
def get_blog(blog_name: Annotated[str, Depends(blog_dependency)]):
    return {"Blog Name": blog_name}

# user_depdency instance of above created call
user_depdendency = GetObjectOr404(users)    

@app.get("/user/{id}")
def get_user(user_name: Annotated[str, Depends(user_depdendency)]): 
    return {"User Name": user_name}