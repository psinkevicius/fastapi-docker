from fastapi import FastAPI

app = FastAPI(title="fastapi-docker")


@app.get("/labas")
def labas():
    return {"message": "labas"}


@app.get("/")
def home():
    return "Namai"
