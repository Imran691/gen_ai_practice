from fastapi import FastAPI

app: FastAPI = FastAPI()    

@app.get("/in/{pname}")

def student_profile(pname: str):
    return {"Student_name": pname}


@app.get("/{org}/student/{sname}")

def student_profile_org(org: str, sname: str):
    return {"Organization": org, "Student_name": sname}