from fastapi import FastAPI, HTTPException, Depends, status
from pydantic import BaseModel
from typing import Annotated


app = FastAPI(
    title="Location Finder API", 
    version="1.0.0",)

# pydantic model to define DB schema
class Location(BaseModel):
    name: str
    location: str


# dictionary of locations as model DB
locations = {
    "zia": Location(name="Zia", location="Karachi"),
    "ali": Location(name="Ali", location="Lahore"),
}

# dependency function
def get_location_or_404(name:str)->Location:
    loc = locations.get(name.lower())
    if not loc:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"No location found for {name}")
    return loc

# path function
# parameter of dependency function & path function endpoint must match (name in this case)
@app.get("/location/{name}")
def get_person_location(name: str, location: Annotated[Location, Depends(get_location_or_404)]):
    return location