from fastapi import FastAPI, Depends
from typing import Annotated

# aprameter of dependency function must match with route endpoint parameter of route function
def dep_func1(num):
    num = int(num)
    num += 1
    return num

def dep_func2(num):
    num = int(num)
    num += 2
    return num

# We pass the multiple dependencies while creating the app
app : FastAPI = FastAPI(dependencies=[Depends(dep_func1), Depends(dep_func2)])

# here we are getting num by URL method
# in pevious examples we used query method
@app.get("/num/{num}")
def get_num(num: int, num1: Annotated[int, Depends(dep_func1)], num2: Annotated[int, Depends(dep_func2)]):
    total = num + num1 + num2
    return f"Total = {total}"

