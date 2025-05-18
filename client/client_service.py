from fastapi import FastAPI, Header, HTTPException

app = FastAPI()

APP_TOKEN = "Nataliia"

@app.get("/")
def root():
    return {"service": "Client Service", "description": "Orchestrates calls to DB and Business Logic services."}

@app.get("/health")
def health_check():
    return {"status": "ok"}

@app.get("/orchestrate")
def orchestrate(authorization: str = Header(None)):
    if authorization != f"Bearer {APP_TOKEN}":
        raise HTTPException(status_code=401, detail="Unauthorized")

    return {"status": "success", "result": "success"}
