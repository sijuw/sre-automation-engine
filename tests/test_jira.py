from app.clients.jira_clients import JiraClient
from app.database.models import Alert

# Create a fake Alert object
alert = Alert(
    title="Payment API Down",
    status="Critical",
    message="Response time exceeded threshold",
    dashboard_url="https://grafana.company.com"
)

client = JiraClient()

client.create_an_incident(alert)