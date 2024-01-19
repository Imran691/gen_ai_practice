from fastapi import FastAPI, Body

app : FastAPI= FastAPI()

@app.post("/hi")   
def greet(who: str = Body(embed=True)):     # embed=True to send the body
    return f"Hello {who} with post method."