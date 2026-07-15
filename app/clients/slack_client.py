import httpx

from app.core.config import settings


class SlackClient:

    def __init__(self):
        self.token = settings.SLACK_BOT_TOKEN

    def send_message(self, channel: str, text: str):

        response = httpx.post(
            "https://slack.com/api/chat.postMessage",
            headers={
                "Authorization": f"Bearer {self.token}"
            },
            json={
                "channel": channel,
                "text": text
            },
            timeout=30
        )

        response.raise_for_status()

        return response.json()

    def send_blocks(self, channel: str, blocks: list):

        response = httpx.post(
            "https://slack.com/api/chat.postMessage",
            headers={
                "Authorization": f"Bearer {self.token}"
            },
            json={
                "channel": channel,
                "blocks": blocks
            },
            timeout=30
        )
        response.raise_for_status()

        return response.json()

    def update_message(self, channel: str, ts: str, blocks: list):
            # Rewritten to use httpx, matching your other methods
            response = httpx.post(
                "https://slack.com/api/chat.update",
                headers={
                "Authorization": f"Bearer {self.token}"
                },
                json={
                    "channel": channel,
                    "ts": ts,
                    "text": "Incident Updated",
                    "blocks": blocks
                },
                timeout=30
            )
            response.raise_for_status()
            return response.json()