# Microservice-Based FastAPI Application with Token Authentication

## Overview

This project demonstrates a simple microservice-based REST application using FastAPI. It consists of three independent services:

- **Client Service**: Entry point for users; handles authentication and orchestrates calls to other services.
- **Business Logic Service**: Simulates a longer-running operation (e.g., ML model inference).
- **Database Service**: Simulates database.


---

## Services

### 1. Client Service
- **Port:** `8000`
- **Endpoints:**
  - `GET /` — Service description
  - `GET /health` — Health check
  - `GET /orchestrate` — Auth-protected; triggers DB → Business → DB flow

### 2. Business Logic Service
- **Port:** `8001`
- **Endpoints:**
  - `GET /` — Service description
  - `GET /health` — Health check
  - `POST /process` — Simulates a long-running task (2-second delay)

### 3. Database Service
- **Port:** `8002`
- **Endpoints:**
  - `GET /` — Service description
  - `GET /health` — Health check

---

## Usage Example

uvicorn db_service:app --port 8002

uvicorn business_service:app --port 8001

uvicorn client_service:app --port 8000
