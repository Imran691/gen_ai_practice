# Parameters can be passed in below mentioned ways
    # In the URL path (As path parameter)
    # As a query parameter, after ? in the URL
    # In HTTP body
    # As an HTTP header

from fastapi import FastAPI

app: FastAPI = FastAPI()    

# Parameter in URL path
# http://localhost:8000/in/imran
@app.get("/in/{pname}")
def student_profile(pname: str):
    return {"Student_name": pname}


# http://localhost:8000/PIAIC/student/imran
@app.get("/{org}/student/{sname}")
def student_profile_org(org: str, sname: str):
    return {"Organization": org, "Student_name": sname}