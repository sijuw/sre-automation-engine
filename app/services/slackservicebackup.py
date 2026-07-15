
from app.database.models import Alert


def build_alert_blocks(alert: Alert) -> list:
    """
    Build a Slack Block Kit message for an alert.
    """

    return [
        {
            "type": "header",
            "text": {
                "type": "plain_text",
                "text": "🚨 Production Alert"
            }
        },
        {
            "type": "section",
            "fields": [
                {
                    "type": "mrkdwn",
                    "text": f"*Title:*\n{alert.title}"
                },
                {
                    "type": "mrkdwn",
                    "text": f"*Status:*\n{alert.status}"
                },
                {
                    "type": "mrkdwn",
                    "text": f"*Jira:*\n{alert.jira_ticket or 'Not Created'}"
                },
                {
                    "type": "mrkdwn",
                    "text": f"*Received:*\n{alert.received_at.strftime('%Y-%m-%d %H:%M:%S')}"
                }
            ]
        },
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": f"*Message:*\n{alert.message}"
            }
        },
        {
            "type": "divider"
        },
        {
            "type": "actions",
            "elements": [
                {
                    "type": "button",
                    "text": {
                        "type": "plain_text",
                        "text": "Create Jira"
                    },
                    "style": "primary",
                    "action_id": "create_jira",
                    "value": str(alert.id)
                },
                {
                    "type": "button",
                    "text": {
                        "type": "plain_text",
                        "text": "Create Jira + Meet"
                    },
                    "action_id": "create_meet",
                    "value": str(alert.id)
                },
                {
                    "type": "button",
                    "text": {
                        "type": "plain_text",
                        "text": "Ignore"
                    },
                    "style": "danger",
                    "action_id": "ignore_alert",
                    "value": str(alert.id)
                }
            ]
        }
    ]

def build_updated_alert_blocks(alert):

    return [
        {
            "type": "header",
            "text": {
                "type": "plain_text",
                "text": "✅ Incident Accepted"
            }
        },
        {
            "type": "section",
            "fields": [
                {
                    "type": "mrkdwn",
                    "text": f"*Title:*\n{alert.title}"
                },
                {
                    "type": "mrkdwn",
                    "text": f"*Status:*\n{alert.status}"
                },
                {
                    "type": "mrkdwn",
                    "text": f"*Jira:*\n{alert.jira_ticket}"
                },
                {
                    "type": "mrkdwn",
                    "text": f"*Handled By:*\n{alert.acknowledged_by}"
                },
                {
                    "type": "mrkdwn",
                    "text": f"*Incident Status:*\n{alert.incident_status}"
                }
            ]
        }
    ]

