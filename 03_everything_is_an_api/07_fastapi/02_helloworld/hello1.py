from fastapi import FastAPI

app : FastAPI = FastAPI()

@app.get("/hi")
def greet() ->str:
    return "Hello World"

@app.get("/hi/{name}")
def greet_with_name(name: str):
    return "Hello World, " + name


# To run the server with pure python command: "python hello1.py"
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("hello1:app", reload=True, port=8000, host="127.0.0.1"  )