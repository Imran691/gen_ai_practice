# Query parameters are name=value strings after ? in URL
# It is passsed as parameter in path funcation

from fastapi import FastAPI 

app : FastAPI = FastAPI()

@app.get("/notifications")
# filter is query parametr
# we will have to pass its valuE after adding a ? in URL as: ?filter=Imran
def notifications(filter: str):
    return {"data" : f"Filter {filter}"}