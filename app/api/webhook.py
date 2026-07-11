import logging
from datetime import datetime


from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.database.models import Alert
from app.schemas import GrafanaAlert

router = APIRouter()

logger = logging.getLogger(__name__)


@router.post("/webhook")
async def receive_alert(
    alert: GrafanaAlert,    
    db: Session = Depends(get_db)
):


# Create a database object
    db_alert = Alert(
        title=alert.title,
        status=alert.status,
        message=alert.message,
        dashboard_url=alert.dashboardURL
    )

    # Save it to SQLite
    try:
        db.add(db_alert)
        db.commit()
        db.refresh(db_alert)
    except Exception as e:
        logger.exception(f"Failed to save alert: {e}")

        return {
        "message": str(e)
    }

    logger.info("=" * 50)
    logger.info("🚨 NEW GRAFANA ALERT RECEIVED")
    logger.info("=" * 50)
    logger.info(f"Title      : {alert.title}")
    logger.info(f"Status     : {alert.status}")
    logger.info(f"Message    : {alert.message}")
    logger.info(f"Dashboard  : {alert.dashboardURL}")
    logger.info(f"Received At: {db_alert.received_at}")
    logger.info("=" * 50)

    return {
        "message": "Alert received successfully"
    }