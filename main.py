from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/sex")
def read_root():
    return {"Hello": "sex"}

@app.get("/dd")
def read_root():
    return {"dd":"ss"}
