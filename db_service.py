from fastapi import FastAPI

app = FastAPI()
database = {}

@app.get("/")
def root():
    return {"service": "Database Service", "description": "Handles reading and writing in-memory data."}

@app.get("/health")
def health_check():
    return {"status": "ok"}