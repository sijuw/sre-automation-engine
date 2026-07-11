from sqlalchemy.orm import Session

from app.database.models import Alert
from app.schemas import GrafanaAlert
from app.services.jira_service import create_jira_ticket

import logging

logger = logging.getLogger(__name__)

def create_alert(
    alert: GrafanaAlert,
    db: Session
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

        return db_alert
    except Exception as e:
        logger.exception(f"Failed to save alert: {e}")
    raise