import logging
import random

logger = logging.getLogger(__name__)


def create_jira_ticket(alert):

    logger.info("Connecting to Jira...")

    if random.choice([True, False]):

        logger.info("Jira ticket created successfully")

        return "INC-1001"

    raise Exception("Jira API unavailable")