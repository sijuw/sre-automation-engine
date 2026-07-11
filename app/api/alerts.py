from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.database.models import Alert
from fastapi import HTTPException
router = APIRouter()

@router.get("/alerts")
async def get_alerts(
    db: Session = Depends(get_db)
):

    alerts = db.query(Alert).all()

    return alerts
@router.get("/alerts/{alert_id}")
async def get_alert(
    alert_id: int,
    db: Session = Depends(get_db)
):
    alert = db.query(Alert).filter(Alert.id == alert_id).first()

    if alert is None:
        raise HTTPException(
            status_code=404,
            detail="Alert not found"
        )

    return alert