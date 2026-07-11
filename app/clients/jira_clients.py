import httpx

from app.core.config import settings

class JiraClient:
    def __init__(self):
        self.base_url = settings.JIRA_URL
        self.email = settings.JIRA_EMAIL
        self.token = settings.JIRA_API_TOKEN

    def who_am_i(self):
        response = httpx.get(
            f"{self.base_url}/rest/api/3/myself",
            auth=(self.email, self.token)
        )
        response.raise_for_status()
        return response.json()

    def get_issue_types(self, project_key):

        response = httpx.get(
        f"{self.base_url}/rest/api/3/project/{project_key}",
        auth=(self.email, self.token)
        )

        response.raise_for_status()

        return response.json()
