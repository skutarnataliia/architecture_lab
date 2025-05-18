import time
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"service": "Business Logic Service", "description": "Performs long-running data processing."}

@app.get("/health")
def health_check():
    return {"status": "ok"}

@app.post("/process")
def process_data(payload: dict):
    time.sleep(2)  # Simulate long processing like ML inference
    processed_result = {"original": payload, "processed": True}
    return processed_result
