from fastapi.testclient import TestClient
from main import app, get_db_session

testing_db = ["DB for testing"]

# Dependency function for test DB
def get_testing_db():
    return testing_db

# Overriding real db dependency with testing db dependency
app.dependency_overrides[get_db_session] = get_testing_db

# Client to connect and send values to DB
client = TestClient(app)

def test_item_should_add_to_db():
    response = client.get(
        "/add-item/?item=sugar",
    )
    assert response.status_code == 200
    assert response.json == {"message": "Item added to DB"}
