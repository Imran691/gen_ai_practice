# GET method is used to only retrieve the data from the server.
# Path or Query parameters can be provided to GET endpoint.
# Values from the request body can not be provided to GET endpoint.

# Request body is used to send data to the server with POST, PUT and PATCH methods.
# Body(embed=True) tells FastAPI that we get the value of who from the JSON-formatted request body.
# embed means that it should look like {"who": "imran"} and not like "imran"
from fastapi import FastAPI, Body

app : FastAPI= FastAPI()

@app.post("/hi")   
def greet(who: str = Body(embed=True)):     # embed=True to send the body
    return f"Hello {who} with post method."