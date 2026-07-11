from fastapi import FastAPI

#import the engine and Base from the database module
from app.database.database import engine
from app.database.models import Base

#import the router we created in the alerts.py file
from app.api.alerts import router as alerts_router

#import the router we created in the webhook.py file

from app.api.webhook import router as webhook_router

# import logging
import logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)


app = FastAPI(
    title="SRE Automation Engine",
    description="Automation platform for incident management",
    version="0.1.0"
)

Base.metadata.create_all(bind=engine)

# register the router with the FastAPI app
app.include_router(webhook_router)
app.include_router(alerts_router)


@app.get("/")
async def root():
    return {
        "application": "SRE Automation Engine",
        "status": "Running",
        "version": "0.1.0"    
}

@app.get("/health")
async def health():
    return {
        "status": "healthy"
    }
