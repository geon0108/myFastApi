from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World ya"}


@app.get("/sex")
def read_root():
    return {"Hello": "sex"}
