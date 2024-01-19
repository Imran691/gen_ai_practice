from fastapi import FastAPI 

app : FastAPI = FastAPI()

@app.get("/notifications")
# filter is query parametr
# we will have to pass its valur after adding a ? in URL as: ?filter=Imran
def notifications(filter: str):
    return {"data" : f"Filter {filter}"}