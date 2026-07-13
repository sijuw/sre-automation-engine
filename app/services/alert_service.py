from sqlalchemy.orm import Session

from app.database.models import Alert
from app.schemas import GrafanaAlert
from app.services.jira_service import create_jira_ticket
from app.repositories.alert_repository import save_alert, update_jira_ticket
from app.clients.slack_client import SlackClient
from app.services.slack_service import build_alert_blocks
from app.core.config import settings
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
    # try:
    #     jira_issue = create_jira_ticket(db_alert)

    # except Exception as e:
    #     logger.exception(f"Jira ticket Creation Failed : {e}")  
    # else:

    #     try:
    #         db_alert = update_jira_ticket(db,db_alert,jira_issue["key"])

    #     except Exception as e:
    #         logger.exception(f"Failed to update Jira ticket in database: {e}")
        logger.info("Sending alert to Slack...")
    try:
        slack_client = SlackClient()
        blocks = build_alert_blocks(db_alert)
            
        response = slack_client.send_blocks(
            channel=settings.SLACK_CHANNEL_ID, 
            blocks=blocks)
        logger.info(f"slack Response: {response}")    
    except Exception as e:
        logger.exception(f"Failed to send alert to Slack: {e}")    
    return db_alert