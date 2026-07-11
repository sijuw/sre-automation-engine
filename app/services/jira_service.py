import logging

logger = logging.getLogger(__name__)


def create_jira_ticket(alert):
    """
    Creates a Jira incident.

    Currently mocked.
    """

    logger.info("Creating Jira ticket...")

    ticket = "INC-1001"

    logger.info(f"Created Jira Ticket: {ticket}")

    return ticket