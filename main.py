from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def root():
    return {"message": "Hello from Cloud Run and this is a test repo!"}


@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/data")
def data():
    return {"data": "sample data"}
