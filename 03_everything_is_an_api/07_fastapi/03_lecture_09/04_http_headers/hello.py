# Passing the greeting argument as an HTTP header

# Start Uvicorn with the command line

# uvicorn hello:app --reload
# Test with HTTPie

# http -v localhost:8000/hi who:Mo

from fastapi import FastAPI, Header

app : FastAPI = FastAPI()
@app.post("/hi")
def greet(who : str = Header()):
    return f"Hello {who}"