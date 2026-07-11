from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import DateTime

from datetime import datetime

from app.database.database import Base


class Alert(Base):

    __tablename__ = "alerts"

    id = Column(Integer, primary_key=True, index=True)

    title = Column(String, nullable=False)

    status = Column(String)

    message = Column(String)

    dashboard_url = Column(String)

    received_at = Column(DateTime, default=datetime.utcnow)

    jira_ticket = Column(String, nullable=True)

    assigned_team = Column(String, nullable=True)

    acknowledged_by = Column(String, nullable=True)

    resolved_at = Column(DateTime, nullable=True)
    incident_status = Column(
        String,
        default="Open"
    )