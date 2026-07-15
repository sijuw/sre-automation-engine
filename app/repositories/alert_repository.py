from sqlalchemy.orm import Session

from app.database.models import Alert


def save_alert(
    db: Session,
    alert: Alert
):

    db.add(alert)
    db.commit()
    db.refresh(alert)

    return alert

def update_alert(
    db: Session,
    alert: Alert
):
    db.commit()
    db.refresh(alert)

    return alert


# def update_jira_ticket(
#     db: Session,
#     alert: Alert,
#     jira_ticket: str
# ):

#     alert.jira_ticket = jira_ticket

#     db.commit()
#     db.refresh(alert)

#     return alert

def get_alert_by_id(
    db: Session,
    alert_id: int
):

    return (
        db.query(Alert)
        .filter(Alert.id == alert_id)
        .first()
    )