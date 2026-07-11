import json
import httpx
import logging
from app.core.config import settings

logger = logging.getLogger(__name__)

class JiraClient:

    def __init__(self):
        self.base_url = settings.JIRA_URL
        self.email = settings.JIRA_EMAIL
        self.token = settings.JIRA_API_TOKEN
        self.project_key = settings.JIRA_PROJECT_KEY

    def who_am_i(self):
        response = httpx.get(
            f"{self.base_url}/rest/api/3/myself",
            auth=(self.email, self.token)
        )
        response.raise_for_status()
        return response.json()

    # Improvement: Default to the class project_key if one isn't provided
    def get_issue_types(self, project_key=None):
        target_key = project_key or self.project_key
        
        response = httpx.get(
            f"{self.base_url}/rest/api/3/project/{target_key}",
            auth=(self.email, self.token)
        )
        response.raise_for_status()
        return response.json()

    def create_an_incident(self, alert):
        description = {
            "type": "doc",
            "version": 1,
            "content": [
                {
                    "type": "paragraph",
                    "content": [
                        {
                            "type": "text",
                            "text": (
                                "Alert generated automatically by the SRE Automation Engine.\n\n"
                                f"Title: {alert.title}\n"
                                f"Status: {alert.status}\n"
                                f"Message: {alert.message}\n"
                                # Note: Ensure this is dashboard_url and not dashboardURL
                                f"Dashboard: {alert.dashboard_url}" 
                            )
                        }
                    ]
                }
            ]
        }

        payload = {
            "fields": {
                "project": {
                    "key": self.project_key
                },
                "summary": f"🚨 {alert.title}",
                "issuetype": {
                    "id": "10003"
                },
                "description": description
            }
        }

        logger.info("Creating Jira Incident...")
        logger.info(json.dumps(payload, indent=4))

        # CRITICAL FIX: Actually send the request to Jira
        response = httpx.post(
            f"{self.base_url}/rest/api/3/issue",
            auth=(self.email, self.token),
            json=payload, # httpx automatically converts the dict to JSON and sets headers
            timeout=30  # Optional: Set a timeout for the request
        )
        logger.info(f"Jira Response Status: {response.status_code}")

        if response.status_code != 201:
            logger.error(response.text)

        # Catch any errors (like a bad project key or issue type)
        response.raise_for_status()

        # Return the Jira response (which contains the new ticket ID and URL)
        return response.json()

  