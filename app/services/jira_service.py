import logging

from app.clients.jira_clients import JiraClient

logger = logging.getLogger(__name__)


def create_jira_ticket(alert):

    logger.info("Connecting to Jira...")

    client = JiraClient()

    issue = client.create_an_incident(alert)

    logger.info(f"Jira Incident Created: {issue['key']}")

    return issue