import logging

from sqlalchemy.orm import Session

from app.repositories.alert_repository import (
    get_alert_by_id, update_alert
)
from app.clients.slack_client import SlackClient
from app.services.slack_service import build_updated_alert_blocks
from app.services.jira_service import create_jira_ticket


logger = logging.getLogger(__name__)


def handle_slack_action(
    action: str,
    alert_id: int,
    db: Session,
    user: str,
    channel: str,
    message_ts: str
):
    """
    Handles Slack button actions.
    """

    alert = get_alert_by_id(db, alert_id)

    if not alert:
        logger.error(f"Alert {alert_id} not found")
        return

    logger.info(f"Processing '{action}' for Alert {alert.id}")

    if action == "create_jira":

        jira_issue = create_jira_ticket(alert)

 

        alert.jira_ticket = jira_issue["key"]
        alert.incident_status = "JIRA_CREATED"
        alert.acknowledged_by = user

        update_alert(
            db,
            alert
        )

        slack_client = SlackClient()

        updated_blocks = build_updated_alert_blocks(alert)

        logger.info(f"Channel: {channel}")
        logger.info(f"Message TS: {message_ts}")

        response = slack_client.update_message(
            channel=channel,
            ts=message_ts,
            blocks=updated_blocks
        )

        logger.info(f"Slack Update Response: {response}")
        logger.info("Slack message updated.")

        logger.info(
            f"Jira Ticket Created: {jira_issue['key']}"
        )


    elif action == "ignore_alert":

        logger.info(f"Processing 'ignore_alert' for Alert {alert_id}")

        alert.incident_status = "IGNORED"

        alert.acknowledged_by = user

        update_alert(
            db,
            alert
        )

        slack_client = SlackClient()

        updated_blocks = build_updated_alert_blocks(alert)

        response = slack_client.update_message(
            channel=channel,
            ts=message_ts,
            blocks=updated_blocks
        )

        logger.info(response)

        logger.info("Alert ignored.")


    elif action == "create_meet":

        logger.info(
            "Google Meet creation not implemented yet."
        )

    else:

        logger.warning(f"Unknown Slack action: {action}")