FROM python:3.11-slim
WORKDIR /app
COPY . .
RUN pip install fastapi uvicorn
EXPOSE 8001

CMD ["uvicorn", "business_service:app", "--host", "0.0.0.0", "--port", "8001"]
