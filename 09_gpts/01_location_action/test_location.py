from fastapi import HTTPException, status
from fastapi.testclient import TestClient

from location import app, Location, get_location_or_404

Locations = {
    "zeeshan": Location(name="zeeshan", location="Karachi"),
    "haider": Location(name="haider", location="Lahore")
}

def fake_get_location_or_404(name: str):
    loc = Locations.get(name.lower())
    if not loc:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Location of {name} not found")
    return loc

app.dependency_overrides[get_location_or_404] = fake_get_location_or_404

client = TestClient(app)

def test_read_location():
    responce = client.get("/location/zeeshan")
    assert responce.status_code == 200
    assert responce.json() == {"name": "zeeshan", "location": "Karachi"}

def test_location_404():
    responce = client.get("/location/john")
    assert responce.status_code == 404

