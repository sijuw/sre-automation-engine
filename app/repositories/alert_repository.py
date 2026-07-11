from sqlalchemy.orm import Session

from app.database.models import Alert


def save_alert(db: Session, alert: Alert):

    db.add(alert)
    db.commit()
    db.refresh(alert)

    return alert

def update_jira_ticket(
    db: Session,
    alert: Alert,
    ticket: str
):

    alert.jira_ticket = ticket

    db.commit()

    db.refresh(alert)

    return alert