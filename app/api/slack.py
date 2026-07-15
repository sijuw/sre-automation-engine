import json
from app.repositories.alert_repository import get_alert_by_id
from fastapi import APIRouter, Request, Depends
from sqlalchemy.orm import Session
from app.services.slack_action_service import handle_slack_action
from app.database.database import get_db

router = APIRouter()


@router.post("/actions")
async def slack_actions(request: Request, db: Session = Depends(get_db)):

    form = await request.form()

    payload = json.loads(form["payload"])

    print(json.dumps(payload, indent=4))

    action = payload["actions"][0]["action_id"]
    alert_id = payload["actions"][0]["value"]
    user = payload["user"]["name"]
    channel = payload["channel"]["id"]
    message_ts = payload["message"]["ts"]
    handle_slack_action(
        action=action,
        alert_id=int(alert_id),
        user=user,
        channel=channel,
        message_ts=message_ts,
        db=db
    )

    return {"ok": True}