from app.clients.slack_client import SlackClient
from app.core.config import settings

client = SlackClient()

blocks = [
    {
        "type": "header",
        "text": {
            "type": "plain_text",
            "text": "🚨 Production Alert"
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "*Title:* Payment API Down\n"
                "*Status:* FIRING\n"
                "*Severity:* Critical"
            )
        }
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
                "action_id": "create_jira"
            },
            {
                "type": "button",
                "text": {
                    "type": "plain_text",
                    "text": "Create Jira + Meet"
                },
                "action_id": "create_meet"
            },
            {
                "type": "button",
                "text": {
                    "type": "plain_text",
                    "text": "Ignore"
                },
                "style": "danger",
                "action_id": "ignore"
            }
        ]
    }
]

response = client.send_blocks(
    channel=settings.SLACK_CHANNEL_ID,
    blocks=blocks
)

print(response)