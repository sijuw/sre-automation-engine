from sqlalchemy.orm import Session

from app.database.models import Alert
from app.schemas import GrafanaAlert
from app.services.jira_service import create_jira_ticket
from app.repositories.alert_repository import save_alert, update_jira_ticket

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
        db_alert = save_alert(db, db_alert)

    
    except Exception as e:
        logger.exception(f"Failed to save alert: {e}")
        raise
    try:
        ticket = create_jira_ticket(db_alert)
        
        db_alert = update_jira_ticket(db,db_alert,ticket)
    except Exception as e:
        logger.exception(f"Jira ticket Creation Failed : {e}")  

    return db_alert