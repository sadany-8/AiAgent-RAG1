from fastapi import FastAPI

app = FastAPI()

@app.get("/welcome")
def welcome ():
    return {"massege":"Welcome To Ai and Python"}

