from fastapi import FastAPI, BackgroundTasks, HTTPException, Request
from time import sleep
import random
from metrics import REQUEST_COUNT, ERROR_COUNT, PROCESSING_TIME, metrics_endpoint
from pydantic import BaseModel

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Dummy pipeline is live."}

@app.get("/health")
def health_check():
    return {"status": "OK"}

@app.get("/metrics")
def prometheus_metrics():
    return metrics_endpoint()

class CitizenData(BaseModel):
    name: str
    age: int
    city: str


@app.post("/submit_data")
def submit_data(payload: CitizenData, background_tasks: BackgroundTasks, request: Request):
    REQUEST_COUNT.labels(endpoint="/submit_data", method=request.method).inc()
    background_tasks.add_task(process_data_task)
    return {"status": "Processing started", "received": payload.dict()}

def process_data_task():
    endpoint = "/submit_data"
    with PROCESSING_TIME.labels(endpoint=endpoint).time():
        try:
            # Simulate work
            sleep(random.uniform(0.2, 1.5))
            # Simulate random error
            if random.random() < 0.1:
                raise Exception("Simulated failure")
        except Exception:
            ERROR_COUNT.labels(endpoint=endpoint).inc()
