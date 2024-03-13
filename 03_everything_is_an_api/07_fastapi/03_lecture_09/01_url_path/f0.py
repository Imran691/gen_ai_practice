from fastapi import FastAPI

app : FastAPI = FastAPI()

@app.get("/")
def index() -> dict:
    return {"message": "Hello World PIAIC"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)